### ----- Código da aula 02 - S202 - L1 --------
from professor import Professor
from aluno import Aluno
from aula import Aula

a=Aluno("Gabriel","1715","GEC","7")
a1=Aluno("Bruno","15","GES","7")
p=Professor("Bruno","Banco De Dados II")

alunos =[a,a1]

aula=Aula("BD 2",alunos,p)

print(aula.getListaPresenca())

    