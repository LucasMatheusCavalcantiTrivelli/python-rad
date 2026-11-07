# Define os modelos de dados (Pessoa, Marca, Veiculo) utilizando
# dataclasses imutáveis para garantir consistência.

from dataclasses import dataclass, field
from datetime import date
from typing import ClassVar, List, Optional  # noqa: UP035


@dataclass(slots=True, frozen=True)
class Pessoa:
    cpf: int
    nome: str
    nascimento: date
    oculos: bool
    pais_origem: ClassVar[str] = "Brasil"
    cidade: Optional[str] = None  # noqa: UP045
    _multas: List[str] = field(default_factory=list)  # noqa: UP006

@dataclass(slots=True, frozen=True)
class Marca:
    id: int
    nome: str
    sigla: str
    pais_origem: ClassVar[str] = "Brasil"

@dataclass(slots=True, frozen=True)
class Veiculo:
    placa: str
    cor: str
    proprietario: Pessoa
    marca: Marca
    pais_origem: ClassVar[str] = "Brasil"

if __name__ == "__main__":
    pessoa1 = Pessoa(cpf=12345678900, nome="Raphel", nascimento=date(1984, 7, 26), oculos=True)
    marca1 = Marca(id=1, nome="Fiat", sigla="FIA")
    veiculo1 = Veiculo(placa="RMS2288", cor="Cinza", proprietario=pessoa1, marca=marca1)

# Aqui poderia colocar prints puchando os valores que queira saber,
# mas todos do "__main__" foram inseridos no programa.