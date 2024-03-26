class instituicão:
    cont = 0
    list = []

    def __init__(self,nome='',dependets = 0):
        self.nome = nome
        self.dependets = dependets  
        instituicão.cont += 1
        instituicão.list.append(self)

    def getnome(self):
        return self.nome
    
    def setnome(self,nome):
        self.nome = nome
    
    def getdependets(self):
        return self.dependets

    def setdependets(self,dependets):
        self.dependets = dependets

    @classmethod
    def quantpessoas(cls):
        return cls.cont
    
    @classmethod
    def listpessoas(cls):
        return cls.list
    
class professores(instituicão):
    
    def __init__(self,nome = '',dependets = 0,qt_turma = 0,vl_turma = 0):
        super().__init__(nome,dependets)
        self.qt_turmas = qt_turma
        self.vl_turma = vl_turma

    def getqt_turma(self):
        return self.qt_turmas
    
    def setqt_turma(self,qt_turmas):
        self.qt_turmas = qt_turmas
    
    def getvl_turma(self):
        return self.vl_turma
    
    def setvl_turma(self,vl_turma):
        self.vl_turma = vl_turma
    
    def rendimento(self):
        redimento = self.qt_turmas * self.vl_turma
        return redimento


class funcinonarios(instituicão):
    def __init__(self,nome = '', dependets = 0,salariofix = 0):
        super().__init__(nome,dependets)
        self.salariofix = salariofix

    def getsalario(self):
        return self.salariofix
    
    def setsalario(self,salariofix):
        self.salariofix = salariofix
    
    def salariozao(self):
        salariototal = self.salariofix + (self.dependets * 100)
        return salariototal


def main():
    #Pessoa 1
    pessoa1 = instituicão("Daniel",2)
    print(f'O {pessoa1.nome} é o nosso primeiro cadastrado e tem {pessoa1.dependets} dependentes')
    
    #Prof 1
    prof1 = professores("dan",2,5,50)
    print(f'O prof {prof1.nome} tem {prof1.qt_turmas} turmas e o valor é de {prof1.vl_turma} por turma')
    print(f'O rendimento do {prof1.nome} foi de: {prof1.rendimento()}')


    #Prof2
    prof2 = professores("Dan",2)
    print(f'O nosso segundo professor {prof2.nome} tem {prof2.dependets} dependentes')

    #Prof 3
    prof3 = professores()
    professores.setnome(prof3,"Daon")
    print(f'O nosso professor {prof3.nome} esta feliz')

    #Prof 4
    prof4 = professores("Serruya",None,3)
    print(f'O professor {prof4.nome} tem {prof4.qt_turmas} turmas')
    professores.setqt_turma(prof4,5)
    print(f'Mas ouve um aumento para {prof4.qt_turmas} turmas')

    #Funcionario 1
    funcionario1 = funcinonarios("Davi",2,500)
    print(f"O nosso funcionario {funcionario1.nome} tem {funcionario1.dependets} e recebe {funcionario1.salariofix} de salario")
    funcinonarios.setsalario(funcionario1,1000)
    print(f'O salario total do funcionario {funcionario1.nome} é {funcionario1.salariozao()}')

    #Funcionario 2
    funcionario2 = funcinonarios("Fernanda",None,1500)
    print(f"A Funcionaria {funcionario2.nome} tem um salario de {funcionario2.salariofix}")

    #Funcionario 3
    funcionario3 = funcinonarios()
    print(f'O nome do funcionario tres é {funcionario3.nome} porque ele não existe (estamos contratando)')
    funcinonarios.setnome(funcionario3,'Noboru')
    print(f'Achamos o novo funcionario e seu nome é {funcionario3.nome}')

    #dados
    quantidade = instituicão.cont
    lista = instituicão.list
    print(f'O total de pessoas cadastrados é de {quantidade}')
    print(f'A lista de pessoas cadastradas é: {lista}')

if __name__== '__main__':
    main()