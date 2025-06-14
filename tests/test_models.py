from decimal import Decimal
from finapp_core.models import Transacao
from finapp_core.storage.sqlite_repo import SQLiteRepo

def test_roundtrip_tmp(tmp_path):
    repo = SQLiteRepo(tmp_path / "test.db")
    t1 = Transacao.nova(Decimal("123.45"), "Salário", "Pagamento")
    repo.adicionar(t1)

    leituras = list(repo.listar())
    assert leituras == [t1]

    repo.remover(t1.id)
    assert list(repo.listar()) == []