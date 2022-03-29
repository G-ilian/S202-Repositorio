from unicodedata import name
from db.database import Database
from helper.WriteAJson import writeAJson

db=Database("Exercicios","Livros")


#Criando os 3 livros assim como pedido
'''
Deixei a criação dos livros comentados para quando executar o código não haver duplicatas
'''

#livros =db.create(1,"Como fazer amigos e influenciar pessoas ","Dale Carnegie",1936,39.9)
#livros =db.create(2,"A revolta de Atlas","Ayn Rand",1957,71.91)
#livros =db.create(3,"O caminho da servidão","F.A Hayek",1944,46.95)

#Atualizando os dados do livro 2
livros=db.update(2,(56.90))
#Vou deletar o livro 3 só para teste

livros=db.delete(3)

livros=db.read()
writeAJson(livros,"Todos os livros")

