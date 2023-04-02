from database import Database

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()
data = db.collection.find()

def TotalGastoB():
    return db.collection.aggregate([ {"$unwind": "$produtos"},
        {"$match": {"cliente_id":"B"}},
        {"$group": {"_id": {"cliente": "$cliente_id"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    ])


def ProdutoMenosVendido():
    return db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
        {"$sort": {"total": 1}},
        {"$limit": 1}
    ])

def ClienteComMenorGasto():
    return db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": {"cliente": "$cliente_id"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        {"$sort": {"_id.data": 1, "total": 1}},
        {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
    ])

def ProdutoVendidoMaisde2Vezes():
    return db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$produtos.nome", "quantidade": {"$sum": "$produtos.quantidade"}}},
        {"$match": {"quantidade": {"$gt":2}}}
    ])