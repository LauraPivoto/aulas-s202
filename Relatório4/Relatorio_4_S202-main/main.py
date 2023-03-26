from save_json import writeAJson
from database import Database

from ProductAnalyzer import *

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()
data = db.collection.find()

result = TotalGastoB()
writeAJson(result, "TotalGastoB")

result2 = ProdutoMenosVendido()
writeAJson(result2, "ProdutoMenosVendido")

result3 = ClienteComMenorGasto()
writeAJson(result3, "ClienteComMenorGasto")

result4 = ProdutoVendidoMaisde2Vezes()
writeAJson(result4, "ProdutoVendidoMaisde2Vezes")