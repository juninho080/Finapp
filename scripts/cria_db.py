from finapp_core.storage.sqlite_repo import SQLiteRepo
repo = SQLiteRepo()
print("finapp.db criado em:", repo.engine.url.database)