Lista = [1, 2, 3, 4, 5, 10, 2, 51, 6, 7, 8]

def bubble_sort(Lista):
    # Percorre toda a lista
    for n in range(len(Lista) - 1, 0, -1):
        for i in range(n):
            # Verifica se o elemento atual é maior que o próximo
            if Lista[i] > Lista[i + 1]:
                # Se sim, troca os elementos de lugar
                Lista[i], Lista[i + 1] = Lista[i + 1], Lista[i]

print(f'Lista desorganizada: {Lista}')
bubble_sort(Lista)
print(f'Lista organizada: {Lista}')
