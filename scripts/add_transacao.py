from decimal import Decimal
from finapp_core.models import Transacao
from finapp_core.storage.sqlite_repo import SQLiteRepo

repo = SQLiteRepo("finapp.db")

t = Transacao.nova(
    valor=Decimal("250.75"),
    categoria="Freelance",
    descricao="Projeto de design"
)
repo.adicionar(t)
for trans in repo.listar():
    print(
        f"{trans.id} | {trans.data} |"
        f"{trans.valor:.2f} | {trans.categoria} | {trans.descricao}"
    )