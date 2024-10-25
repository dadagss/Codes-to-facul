import multiprocessing as mp
import time

# Daniel Guimarães Silva
# 22302201
# Turma B
# 1.	Irei criar o array arr com 100 posições
# 2.	Criarei a função de calcular o fatorial inicializando o array fatorial sem nada, e para cada numero i dentro de arr irei criar uma variável fat = 1 e para cada c de 1 até i + 1 irei multiplicar fat por c, fazendo com que o numero se multiplique por 1 ate ele mesmo
# 3.	Irei armazenar dentro da lista fatorial.
# 4.	Irei criar a função fatoriar passando o arr e primeiro irei verificar se ele esta vazio, caso não, ele vai dividir arr em partes iguais dividindo-o pela numero de cores disponíveis
# 5.	Depois ira pegar os intervalos verificando se cada parte esta de tamanho igual e caso o numero seja impar e sobre um numero ele ira agregar a uma parte
# 6.	Irei usar o mp.pool para processar o criarfatorial do começo ao fim e armazenar na variável resultados
# 7.	Irei inicializar a lista final trazendo cada fatorial nas sublistas criadas e retornarei ele.
# 8.	Em seguida irei printar cada fatorial e seu tempo de execução

#nota: o tempo de execução na minha maquina deu 0.22 segundos de forma paralela
#nota: de forma sequencial foi 0.0 segundos

cores = mp.cpu_count() - 1

#criando o array
n = 100
arr = []
for i in range(1, n+1):
    arr.append(i)

def criarfatorial(arr):
    fatorial = []
    for i in arr:
        fat = 1
        for c in range(1, i + 1):
            fat *= c
        fatorial.append(fat)
    return fatorial

def fatoriar(arr):
    if len(arr) < 1:
        print("O array esta vazio")
        return 0
    
    tamanho_parte = len(arr) // cores
    intervalos = [(i * tamanho_parte, (i + 1) * tamanho_parte if i < cores - 1 else len(arr)) for i in range(cores)]
    
    with mp.Pool(processes=cores) as pool:
        resultados = pool.map(criarfatorial, [(arr[start:end]) for start, end in intervalos ])

    fatoriais_completos = [fat for sublista in resultados for fat in sublista]

    return fatoriais_completos

def main():
    tempo_inicio = time.time()
    fatoriais = fatoriar(arr)
    tempo_final = time.time()
    print("Os fatoriais são:")
    for i in fatoriais:
        print(f"{i}")
    print(f"Tempo de execução: {tempo_final - tempo_inicio:.2f} segundos")

if __name__ == "__main__":
    main()