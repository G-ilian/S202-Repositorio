from professor import Professor
from aluno import Aluno

class Aula(Professor,Aluno):
    def __init__(self,assunto,aluno,professor):
        self.assunto=assunto
        self.professor=professor
        self.aluno=aluno

    def getListaPresenca (self):
        
        t=f"Aula de {self.assunto} \nProfessor: {self.professor.nome}\nAlunos Presentes: "
        
        for alunos in self.aluno:
            t=t+alunos.toString()
        
        return t
        
        


