from abc import ABC, abstractmethod
from typing import Iterable
from finapp_core.models import Transacao

class Repositorio(ABC):
    """Contrato que TODO repositório coincreto deve cumprir."""

    @abstractmethod
    def adicionar(self, t: Transacao) -> None: ...

    @abstractmethod
    def listar(self) -> Iterable[Transacao]: ...

    @abstractmethod
    def remover(self, transacao_id) -> None: ...