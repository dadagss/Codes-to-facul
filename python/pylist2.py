import time

n = 100
arr = []
for i in range(1, n+1):
    arr.append(i)


def criarfatorial(lista):
    fatorial = []
    for i in lista:
        fat = 1
        for c in range(1, i + 1):
            fat *= c
        fatorial.append(fat)
    return fatorial

def main(arr):
    tempo_inicio = time.time()
    fatoriais = criarfatorial(arr)
    tempo_final = time.time()
    for i in fatoriais:
        print(f'Os números fatoriais são: {i}')
    print(f"Tempo de execução: {tempo_final - tempo_inicio:.2f} segundos")

if __name__ == "__main__":
    main(arr)
