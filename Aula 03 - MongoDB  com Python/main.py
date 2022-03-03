from bson.son import SON
from db.database import Database

db = Database()

pokemon=db.getAllPokemons()

print(pokemon)