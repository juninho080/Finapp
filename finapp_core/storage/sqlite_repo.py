from pathlib import Path
from typing import Iterable
from uuid import UUID

from sqlalchemy import (
    Column, Date, Numeric, String,
    create_engine, select, delete
)
from sqlalchemy.orm import DeclarativeBase, Session

from finapp_core.models import Transacao
from .base import Repositorio


class Base(DeclarativeBase):
    """Base para o mapeamento ORM."""
    pass


class _TransacaoDB(Base):
    __tablename__ = "transacoes"

    id = Column(String(36), primary_key=True)
    data = Column(Date, nullable=False)
    valor = Column(Numeric(14, 2), nullable=False)
    categoria = Column(String(40), nullable=False)
    descricao = Column(String(120), default="")

    def para_modelo(self) -> Transacao:
        """Converte o registro ORM para a dataclass Transacao."""
        return Transacao(
            id=UUID(self.id),
            data=self.data,
            valor=self.valor,
            categoria=self.categoria,
            descricao=self.descricao,
        )


class SQLiteRepo(Repositorio):
    """Persistência local em arquivo .db (camada 2)."""

    def __init__(self, caminho_db: str | Path = "finapp.db") -> None:
        # Inicializa o engine SQLite e cria tabelas
        self.engine = create_engine(f"sqlite:///{caminho_db}", echo=False)
        Base.metadata.create_all(self.engine)

    def adicionar(self, t: Transacao) -> None:
        """Adiciona uma transação ao banco."""
        with Session(self.engine) as session:
            session.add(
                _TransacaoDB(
                    id=str(t.id),
                    data=t.data,
                    valor=t.valor,
                    categoria=t.categoria,
                    descricao=t.descricao,
                )
            )
            session.commit()

    def listar(self) -> Iterable[Transacao]:
        """Retorna todas as transações cadastradas."""
        with Session(self.engine) as session:
            stmt = select(_TransacaoDB)
            for db_obj in session.scalars(stmt):
                yield db_obj.para_modelo()

    def remover(self, transacao_id: UUID) -> None:
        """Remove uma transação pelo seu ID."""
        with Session(self.engine) as session:
            session.execute(
                delete(_TransacaoDB).where(_TransacaoDB.id == str(transacao_id))
            )
            session.commit()