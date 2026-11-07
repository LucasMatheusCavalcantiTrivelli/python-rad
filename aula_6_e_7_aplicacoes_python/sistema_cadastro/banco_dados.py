# Implementa a camada de persistência com SQLite: criação de tabelas,
# chaves estrangeiras, inserção e atualização segura.

import sqlite3
from pathlib import Path
from typing import Any, ClassVar

from logger_config import exception, info, logger  # noqa: F401
from modelos_dados import Marca, Pessoa, Veiculo  # noqa: F401


class BancoDeDados:
    CAMPOS_PESSOAS_PERMITIDOS: ClassVar[frozenset[str]] = frozenset({"nome", "nascimento", "oculos"})

    def __init__(self, caminho_banco: Path):
        self.caminho_banco = caminho_banco
        self.conn: sqlite3.Connection | None = None

    def conectar(self) -> None:
        try:
            self.conn = sqlite3.connect(self.caminho_banco)
            self.conn.row_factory = sqlite3.Row
            self.conn.execute("PRAGMA foreign_keys = ON")
            logger.info("Conexão com o banco realizada com sucesso.")

        except sqlite3.Error:
            logger.exception("Erro ao conectar ao banco de dados.")
            raise

    def _obter_conexao(self) -> sqlite3.Connection:
        if self.conn is None:
           raise RuntimeError(
               "Banco de dados não conectado. "
                "Execute conectar() antes de realizar operações."
                )
        return self.conn

    def criar_tabelas(self) -> None:
        conn = self._obter_conexao()

        try:
            with conn:
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS Pessoa (
                        cpf TEXT PRIMARY KEY,
                        nome TEXT NOT NULL,
                        nascimento TEXT NOT NULL,
                        oculos INTEGER NOT NULL
                            CHECK (oculos IN (0, 1))
                    )
                    """
                )
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS Marca (
                        id INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        sigla TEXT NOT NULL
                    )
                    """
                )
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS Veiculo (
                    placa TEXT PRIMARY KEY,
                    cor TEXT NOT NULL,
                    cpf_proprietario TEXT NOT NULL,
                    id_marca INTEGER NOT NULL,
                    FOREIGN KEY (cpf_proprietario)
                        REFERENCES Pessoa(cpf)
                        ON UPDATE CASCADE
                        ON DELETE RESTRICT,
                    
                    FOREIGN KEY (id_marca)
                        REFERENCES Marca(id)
                        ON UPDATE CASCADE
                        ON DELETE RESTRICT
                    )
                    """
                )
            logger.info("Tabelas criadas com sucesso.")

        except sqlite3.IntegrityError:
            logger.exception("Erro de integridade durante a criação das tabelas.")
            raise

        except sqlite3.OperationalError:
            logger.exception("Erro operacional durante a criação das tabelas.")
            raise

        except sqlite3.DatabaseError:
            logger.exception("Erro de banco durante a criação das tabelas.")
            raise

        except sqlite3.Error:
            logger.exception("Erro geral do SQLite durante a criação das tabelas.")
            raise

    def adicionar_coluna_motor(self) -> None:
        conn = self._obter_conexao()
        try:
            colunas = conn.execute(
                "PRAGMA table_info(Veiculo)"
            ).fetchall()

            nome_colunas = {
                coluna["name"]
                for coluna in colunas
            }

            if "motor" in nome_colunas:
                logger.info("A coluna 'motor' já existe na tabela Veiculo.")
                return

            with conn:
                conn.execute(
                    """
                    ALTER TABLE Veiculo
                    ADD COLUMN motor TEXT
                    """
                )

            logger.info("Coluna 'motor' adicionada com sucesso.")

        except sqlite3.Error:
            logger.exception(
                "Erro ao adicionar coluna à tabela Veiculo."
            )
            raise

    def inserir_pessoa(self, pessoa: Pessoa) -> None:
        conn = self._obter_conexao()
        try:
            with conn:
                conn.execute(
                    """INSERT INTO Pessoa (
                        cpf,
                        nome,
                        nascimento,
                        oculos
                    )
                    VALUES (?, ?, ?, ?)""",
                    (
                        pessoa.cpf,
                        pessoa.nome,
                        pessoa.nascimento.isoformat(),
                        int(pessoa.oculos),
                    ),
                )

            logger.info(
                "Pessoa %s inserida com sucesso.",
                pessoa.cpf, 
            )

        except sqlite3.IntegrityError:
            logger.exception(
                "Erro de integridade ao inserir pessoa %s.",
                pessoa.cpf,
            )
            raise

        except sqlite3.Error:
            logger.exception(
                "Erro ao inserir pessoa %s.",
                pessoa.cpf,
            )
            raise

    def atualizar_pessoa(self, pessoa: Pessoa) -> None:
        conn = self._obter_conexao()
        try:
            with conn:
                cursor = conn.execute(
                    """UPDATE Pessoa
                    SET
                        nome= ?,
                        nascimento = ?,
                        oculos = ?
                    WHERE cpf = ? """,
                    (
                        pessoa.nome,
                        pessoa.nascimento.isoformat(),
                        int(pessoa.oculos),
                        pessoa.cpf,
                    ),
                )

            if cursor.rowcount == 0:
                logger.warning(
                    "Nenhuma pessoa encontrada com CPF %s.",
                    pessoa.cpf,
                )
                return

            logger.info(
                "Pessoa %s atualizada com sucesso.",
                pessoa.cpf,
            )

        except sqlite3.Error:
            logger.exception(
                "Erro ao atualizar pessoa %s.",
                pessoa.cpf,
            )
            raise

    def atualizar_pessoa_campos(self, cpf: str, **campos: Any, ) -> None:
        conn = self._obter_conexao()

        if not campos:
            raise ValueError("Informe pelo menos um campo para atualizar.")

        campos_invalidos = (set(campos) - self.CAMPOS_PESSOAS_PERMITIDOS)

        if campos_invalidos:
            raise ValueError(
                "Campos não permitidos: "
                + ", ".join(sorted(campos_invalidos))
            )

        atribuicoes: list[str] = []
        valores: list[Any] = []

        for nome_campo, valor in campos.items():
            atribuicoes.append(f"{nome_campo} = ?")
            if nome_campo == "nascimento":
                valor = valor.isoformat()
            elif nome_campo == "oculos":
                valor = int(valor)
            valores.append(valor)
        valores.append(cpf)
        sql = f"""UPDATE Pessoa SET {", ".join(atribuicoes)} WHERE cpf = ? """
        try:
            with conn:
                cursor = conn.execute(sql, tuple(valores),)
            if cursor.rowcount == 0:
                logger.warning("Pessoa %s não encontrada.", cpf,)
                return

            logger.info("Pessoa %s atualizada com sucesso.", cpf,)

        except sqlite3.Error:
            logger.exception("Erro ao atualizar pessoa %s.", cpf,)
            raise

if __name__ == "__main__":
    from datetime import date
    
    pasta_atual = Path(__file__).resolve().parent
    db = BancoDeDados(pasta_atual / "banco_de_teste.db")
    db.conectar()
    db.criar_tabelas()
    
    nova_pessoa = Pessoa(cpf="12345678900", nome="Raphael", nascimento=date(1984, 7, 26), oculos=True)
    db.inserir_pessoa(nova_pessoa)
    
    db.atualizar_pessoa_campos(cpf="12345678900", nome="Raphael Alterado", oculos=False)
    
    db.adicionar_coluna_motor()
    
    print("Testes do CRUD finalizados!")