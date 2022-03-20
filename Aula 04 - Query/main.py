from db.database import Database
from helper.WriteAJson import writeAJson



db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

# 1º Query
fraquezas = ["Fighting", "Psychic"]
pokemons_fraquezas = db.executeQuery({"weaknesses":{"$in": fraquezas},"next_evolution":{"$exists":True}})
writeAJson(pokemons_fraquezas,"Pokemons Fraquezas")

# 2º Query
pokemons_sem_fraquezas = db.executeQuery({"weaknesses": {"$exists": True}})
writeAJson(pokemons_fraquezas,"Pokemons sem campo weaknesses")

# 3º Query
evol_anteriores = ["Nidoran(Female)","Nidorina","Zubat"]
pokemons_evolucao_anterior=db.collection.find({"prev_evolution":{"$in":evol_anteriores}},{"name":True})
writeAJson(pokemons_evolucao_anterior,"Nomes pokemons evol anterior")

# 4º Query
pokemons_voa_eletrico = db.executeQuery({"$or": [{"type":"Flying"},{"weaknesses": "Electric"}]})
writeAJson(pokemons_voa_eletrico,"Pokemons que voam e tem fraqueza a eletricidade ")

# 5º Query
pokemons_ovo=db.executeQuery({"egg":"Not in Eggs"})
writeAJson(pokemons_ovo,"Pokemons que vem de ovos")