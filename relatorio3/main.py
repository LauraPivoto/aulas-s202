from pokedex import Database
from save_json import writeAJson

db = Database(database="dex", collection="pokemons")
db.resetDatabase()

pokemons = db.collection.find()
for pokemon in pokemons:  # printando ela
    print(pokemon)

# pesquisa por pokemons com defesa menor ou igual que 10
pokemon = db.collection.find({"base.Defense": {"$lte": 10}})
writeAJson(pokemon, "defense10")

# pesquisa por pokemons tipo fogo
pokemon = db.collection.find({"type": "Fire"})
writeAJson(pokemon, "firepokemons")


# pokemons de nome de 8 letras ou menos
#não mudei o nome do arquivo pois queria 10 letras no tamanho do nome mas n consegui
def get_8_letters(collection):
    names = collection.find({}, {"name": 1})
    eight_letters = []
    for name in names:
        if len(name["name"].keys()) <= 8:
            if all(len(word) <= 8 for word in name["name"].values()):
                eight_letters.append(name["name"].values())
    return eight_letters


writeAJson(get_8_letters(db.collection), "tenlettersnames")

#pokemom com corrida 80 ou menos
pokemon = db.collection.find({"base.Speed": {"$lte": 80}})
writeAJson(pokemon, "speed80")

#pokemom com o nome japones igual a "トランセル"
pokemon = db.collection.find({"name.japanese": {"$lte": "トランセル"}})
writeAJson(pokemon, "japanese")