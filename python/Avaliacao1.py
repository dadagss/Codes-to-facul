from abc import ABC, abstractclassmethod


class Animal(ABC):
    objts = 0
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Animal.objts += 1

    def getnome(self):
        return self.nome

    def setnome(self, nova_nome):
        self.nome = nova_nome

    def getidade(self):
        return self.idade

    def setidade(self, nova_idade):
        self.idade = nova_idade

    @classmethod
    def totalobjts(cls):
        return cls.objts

    @abstractclassmethod
    def barulho(self):
        pass


class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def getraca(self):
        return self.raca

    def setraca(self, nova_raca):
        self.raca = nova_raca

    def barulho(self):
        return "AUAU!"


class Gato(Animal):
    def __init__(self, nome, idade, raca, cor):
        super().__init__(nome, idade)
        self.raca = raca
        self.cor = cor

    def getcor(self):
        return self.v

    def setv(self, nova_cor):
        self.v = nova_cor

    def getraca(self):
        return self.raca

    def setraca(self, nova_raca):
        self.raca = nova_raca

    def barulho(self):
        return "Meow"


if __name__ == "__main__":
    dog1 = Cachorro("Luke", 1, "Papillon")
    print(f'O nome do meu cachorro é {dog1.nome}, ele tem {dog1.idade} e é da raça {dog1.raca}')
    print(f'Total de objetos instanciados: {Animal.totalobjts()}')
    print(dog1.barulho())
    dog1.setnome("Bolinho")
    print(f'O nome do meu cachorro e {dog1.nome}')
    dog1.setidade(5)
    print(f'Sua idade é de {dog1.idade}')
    dog1.setraca("Golden-Retriver")
    print(f'Sua raça é {dog1.raca}')

    cat1 = Gato("Perigo",3,"Vira-lata","listrada")
    print(f'O nome do meu gato é {cat1.nome}, ele tem {cat1.idade} e é {cat1.raca} da cor {cat1.cor}')
    print(cat1.barulho())
    print(f'Total de objetos instanciados: {Animal.totalobjts()}')
    cat1.setcor("Laranja")
    print(f"A cor do meu gato é {cat1.cor}")