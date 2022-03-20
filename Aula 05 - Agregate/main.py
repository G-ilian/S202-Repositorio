from db.database import Database
from helper.WriteAJson import writeAJson
from dataset.produto_database import dataset
from dataset.pessoa_dataset import dataset as cliente

compras = Database(database="database", collection="produtos", dataset=dataset)
compras.resetDatabase()

cliente = Database(
    database="database",
    collection="pessoas",
    dataset=cliente
)
cliente.resetDatabase()

result1 = compras.collection.aggregate([
    {"$project": {
        "_id": 0,
        "cliente": 1,
        "desconto": {
            "$cond": {"if": {"$gte": ["$total", 10]}, "then": 0.1, "else": 0.05}
        }
    }}
])








