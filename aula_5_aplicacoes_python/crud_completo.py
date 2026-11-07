# Demonstra o SQLAlchemy 2.0 (sintaxe moderna): cria um banco SQLite local,
# define modelo com Mapped e realiza consultas com select().

# Rodar múltiplas vezes vai duplicar os dados do banco, a menos que você
# apague o arquivo banco_dados.db antes de rodar novamente.

import os

from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(DIRETORIO_ATUAL, 'banco_dados.db')
engine = create_engine(f'sqlite:///{CAMINHO_BANCO}', echo = True)

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key = True)
    nome: Mapped[str] = mapped_column()
    idade: Mapped[int] = mapped_column()

    def __repr__(self) -> str:
        return f"Usuario(id={self.id}, nome={self.nome}, idade={self.idade})"

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)

with Session() as session:
    usuario1 = Usuario(nome = 'Raphael', idade = 42)
    usuario2 = Usuario(nome = 'Leticia', idade = 40)
    session.add_all([usuario1, usuario2])

    session.commit()

    stmt = select(Usuario)
    usuarios = session.scalars(stmt).all()

    for usuario in usuarios:
        print(usuario)