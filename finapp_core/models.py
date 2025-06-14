from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from uuid import uuid4, UUID

@dataclass(slots=True, frozen=True)
class Transacao:
    """Representa um lançamento financeiro único."""
    id: UUID
    data: date
    valor: Decimal      #positivo = receita; negativo = despesa
    categoria: str
    descricao: str = ""

    @staticmethod
    def nova (valor: Decimal, categoria: str, descricao: str = "",
              data: date | None = None) -> "Transacao":
        """Factory que gera id e data automaticamente."""
        return Transacao(
            id=uuid4(),
            data=data or date.today(),
            valor=valor,
            categoria=categoria,
            descricao=descricao,
        )