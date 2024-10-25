#- Implemente:
#1- Crie a classe Livro com os atributos: título, autor, páginas e preço.
#2- Crie o método construtor (init) que recebe quatro parâmetros e
#   use pelo menos um desses parâmetros com valor default (padrão)
#3- Crie o objeto livro1 passando os quatro argumentos, teste
#4- Crie o objeto livro2 passando apenas três argumentos, teste
#5- Crie pelo menos um método get e pelo menos um método set, teste
#6- No item anterior, faça crítica no método set, teste
#7- Crie o método funcional aumento_preco com o objetivo de atualizar o preço do livro.
  #Esse método recebe o valor do aumento e atualiza o atributo preco. Teste
#8- Use (teste) todos os métodos criados na classe Livro para os objetos livro1 e livro2.
#9- Crie o método mostra_dados, mostra todos os valores dos atributos
#10- Crie o método funcional aumento_porcentagem para atualizar o preço
#11- Crie o mètodo __str__
#12- Elabore o enunciado de mais um método funcional importante para a classe

#13- O sistema precisa informar quantos livros foram cadastrados.
#14- Crie o método de classe para recuperar essa informação



class Livros:
    cont = 0
    quant = []


    @classmethod
    def qt_livros(cls):
        return cls.cont
    
    @classmethod
    def get_lista(cls):
        return cls.quant

    def __init__(self,titulo, autor, paginas, preco = 0):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.paginas = paginas
        Livros.cont += 1
        Livros.quant.append(self)
    #mexer no titulo
    def mudartitulo(self,novo_titulo):
        self.titulo = novo_titulo
    
    #aumentar o preço
    def aumentarpreco(self,novo_preco):
        self.preco = self.preco + novo_preco
    
    def testes(self,titulo,autor,paginas,preco):
        self.titulo = get.titulo
        self.autor = get.autor
        self.preco = get.preco
        self.paginas = get.preco
    
    #aumentar preço porcentagem
    def aumentarpercent(self, novo_preco):
        self.preco = self.preco + (self.preco * novo_preco)

    #metodo __str__
    def __str__(self):
        dados = f'{self.titulo}, {self.autor}, {self.paginas}, {self.preco}'
        return dados

def main():
    livro1 = Livros("As cronicas de Dandan","Dan",69,100)
    livro2 = Livros("Dani e a marola filosofal","Dani",96)

    print(livro1)
    print(livro2)
    
    #printar os nomes

    print(livro1.titulo)
    livro1.mudartitulo("Happy e a felicidade universal")
    print(livro1.titulo)
    
    #printar tudo

    print(livro1.testes)
    
    #numero de livros cadastrados
    print(f'Número de livros cadastrados: {Livros.qt_livros()}')
    print(f'Lista de livros cadastrados: {Livros.get_lista()}')
main()