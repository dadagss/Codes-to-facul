import multiprocessing as mp
import numpy as np
import time

#A gente usa a função array para criar um array de 1 milhão de caracteres
tamanho = 1_000_000
arr = np.arange(tamanho)

#Essa função sera usada para calcular a soma de uma das partes do nosso resultado
def soma(comeco, fim, arr, resultado):
    soma_parcial = np.sum(arr[comeco:fim])
    resultado.put(soma_parcial)

#essa sera nossa função principal
def soma_pararela(arr):
    #define o numero de cores da CPU
    num_cores = mp.cpu_count()
    #Define o tamanho de cada parte
    tamanho_parte = len(arr) // num_cores 
    #Guarda os processos em uma fila
    aguardando = mp.Queue()
    processos = []

    for i in range (num_cores):
        #Pega o indice inicial do processo
        comeco = i * tamanho_parte
        #pega o indice final do processo e garante que não sobre nenhum e caso contrario ele ira cobrir a parte restante
        fim = (i + 1) * tamanho_parte if i < num_cores - 1 else len(arr)
        #cria um processo para a função soma, calculando do começo ao fim de cada parte
        p = mp.Process(target=soma, args =(comeco, fim, arr, aguardando))
        #adiciona o processo a lista
        processos.append(p)
        #inica a execução do processo p fazendo ele rodar em paralelo aos demais
        p.start()

    for p in processos:
        #garante que todos os processos tenham sido calculados antes de prosseguir
        p.join()

    soma_total = 0
    #enquando a fila aguardando não estiver vazia este loop continuara guardando as somas parciais
    while not aguardando.empty():
        #adicona cada soma parcial da fila aguardando e adiconaa na soma_total
        soma_total += aguardando.get()
    
    return soma_total

def main():
    tempo_inicio = time.time()
    soma_total = soma_pararela(arr)
    tempo_final = time.time()
    print(f'Soma total : {soma_total}')
    print(f'Tempo de execução: {tempo_final - tempo_inicio:.2f} segundos')

if __name__ == "__main__":
       main()
       #Meu resultado final de 499999500000 na minha maquina
       #E o tempo de execução 1.67 segundos