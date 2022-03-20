from db.database import Database
from helper.WriteAJson import writeAJson
from dataset.pessoa_dataset import dataset as pessoa_dataset
from dataset.carro_dataset import dataset as carro_dataset
from dataset.produto_database import dataset as produto_dataset

pessoas = Database(
    database="database",
    collection="pessoas",
    dataset=pessoa_dataset
)
pessoas.resetDatabase()

carros = Database(
    database="database",
    collection="carros",
    dataset=carro_dataset
)

carros.resetDatabase()

compras = Database(
    database="database",
    collection="produtos",
    dataset=produto_dataset
)

compras.resetDatabase()

result1 = carros.collection.aggregate([
    {"$lookup":
        {
            "from": "pessoas",  # outra colecao
            "localField": "dono_id",  # chave estrangeira
            "foreignField": "_id",  # id da outra colecao
            "as": "dono"  # nome da saida
        }
     }
])

# Exercício Lookup entre pessoas e compras
result2=compras.collection.aggregate([
    {"$lookup":
        {
            "from": "pessoas",  # outra colecao
            "localField": "cliente_id",  # chave estrangeira
            "foreignField": "_id",  # id da outra colecao
            "as": "Clientes"  # nome da saida
        }
     },
    {"$group": {"_id": "$Clientes", "total": {"$sum": "$total"} } }, # formata os documentos
    {"$sort": {"total": 1} }, # ordena os documentos
    {"$unwind": '$_id'},
    
    #Project qua apresenta nome das pessoas em caso da compra ter um total maior que 10
    {"$project": {
        "_id": 0,
        "nome": "$_id.nome",
        "total":1,
        "desconto": {
            "$cond": {"if": {"$gte": ["$total", 10]}, "then": True, "else": False}
        }
    }}
])


writeAJson(result2, "Exercicios")




