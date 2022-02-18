#Importando a classe em questão

from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self,nome,especialidade):
        super().__init__(nome)
        self.especialidade=especialidade
    def toString(self):
        return f'''
        Professor: {self.nome}
        Especialidade: {self.especialidade}
        '''



