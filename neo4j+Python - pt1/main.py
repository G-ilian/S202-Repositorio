from venv import create
from helper.write_a_json import write_a_json
from db.database import Graph


db = Graph("bolt://3.82.126.215:7687", "neo4j", "leaps-knowledge-businesses")

data = db.execute_query("match (n) return n")
write_a_json(data, "all_data")


#data = db.execute_query("create (n:Person {name: 'John'}) return n")


def limpa_Bd():
    data=db.execute_query("MATCH (n) DETACH DELETE n")  
    return data
def create_professor(nome,idade,area):
    data=db.execute_query("create (n:Professor {name:$nome,idade:$idade,area:$area}) return n",{'nome':nome,'idade':idade,'area':area})
    return data

def create_materia(disc,assunto):
    data=db.execute_query("create(m:Materia {disciplina:$disciplina,assunto:$assunto}) return m",
    {'disciplina':disc,'assunto':assunto})
    return data


def leciona(nome,disciplina,ano):
    data=db.execute_query("MATCH(p:Professor{name:$name}),(m:Materia{disciplina:$disciplina})CREATE(p)-[:LECIONA{ano:$ano}]->(m)",
    {"name":nome,"disciplina":disciplina,"ano":ano})
    return data

# Limpando o BD
limpa=limpa_Bd()
# Professores
professor1=create_professor('Renzo',40,'Computação')
professor2=create_professor('Chris',36,'Computação')
professor3=create_professor('Marcelo',35,'Computação')
professor4=create_professor('Leovani',52,'Ciências Humanas')

# Materias
materia1=create_materia('C012','Sistemas Operacionais')
materia2=create_materia('C210','Inteligência Artficial')
# Relações
relacao1=leciona('Renzo','C012',2018)
relacao2=leciona('Marcelo','C210',2020)

