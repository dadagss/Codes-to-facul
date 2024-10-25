# Daniel Guimarães
# 22302201
# Turma B
# 1.	Primeiro passo irei coletar os elementos da lista e irei inicializar a função somarlist, com a lista. 
# 2.	Irei inicializar fazendo a contagem de cores e  separando a lista de forma paralela.
# 3.	Irei checar se a lista não esta vazia e caso ela tenha mais de 1 elemento irei fazer a divisão de elementos por core e realizar a soma de cada um separadamente e armazenar o resultado na memoria
# 4.	Logo irei pegar os resultados e juntar em uma soma so na variável soma.
# 5.	Retornarei ela para o sistema.



import multiprocessing as mp
import time

n = 1000000
arr = []
for i in range(1, n+1):
    arr.append(i)

def soma_parcial(start, end, arr):
    return sum(arr[start:end])

def somararr(arr):
    cores = mp.cpu_count()
    
    if len(arr) <= 1:
        print("A lista não pode ser somada")
        return 0
    
    tamanho_parte = len(arr) // cores
    intervalos = [(i * tamanho_parte, (i + 1) * tamanho_parte if i < cores - 1 else len(arr)) for i in range(cores)]

    with mp.Pool(processes=cores) as pool:
        resultados = pool.starmap(soma_parcial, [(start, end, arr) for start, end in intervalos])
    
    return sum(resultados)

def main():
    tempo_inicio = time.time()
    soma_total = somararr(arr)  
    tempo_final = time.time()
    print(f'Soma total : {soma_total}')
    print(f'Tempo de execução: {tempo_final - tempo_inicio:.2f} segundos')

if __name__ == "__main__":
    main()
