#Importando a classe em questão
from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self,nome,matricula,curso,periodo) -> None:
        super().__init__(nome)
        self.matricula=matricula
        self.curso=curso
        self.periodo=periodo

    def toString(self):
        return f'''
        Nome: {self.nome}
        matricula: {self.matricula}
        curso: {self.curso}
        periodo: {self.periodo}
        '''
       

