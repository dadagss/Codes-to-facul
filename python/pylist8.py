def gerar_subconjuntos(lst, tamanho_subconjunto):
    # Função auxiliar que gera todos os subconjuntos de tamanho fixo
    subconjuntos = []
    
    def backtrack(inicio, subconjunto_atual):
        # Se o subconjunto atual atingir o tamanho desejado, adiciona à lista de subconjuntos
        if len(subconjunto_atual) == tamanho_subconjunto:
            subconjuntos.append(subconjunto_atual[:])
            return
        
        # Gera subconjuntos recursivamente
        for i in range(inicio, len(lst)):
            subconjunto_atual.append(lst[i])
            backtrack(i + 1, subconjunto_atual)
            subconjunto_atual.pop()
    
    # Inicia a geração de subconjuntos
    backtrack(0, [])
    return subconjuntos

def calcular_medias_subconjuntos(lst, tamanho_subconjunto):
    # Gera todos os subconjuntos de tamanho fixo
    subconjuntos = gerar_subconjuntos(lst, tamanho_subconjunto)
    
    # Calcula a média aritmética de cada subconjunto
    medias = []
    for subconjunto in subconjuntos:
        media = sum(subconjunto) / tamanho_subconjunto
        medias.append(media)
    
    return medias

def main():
    # Exemplo de lista
    lst = [1, 2, 3, 4, 5]
    
    # Definir o tamanho do subconjunto
    tamanho_subconjunto = 3
    
    # Chama a função e imprime o resultado
    medias = calcular_medias_subconjuntos(lst, tamanho_subconjunto)
    print("Médias dos subconjuntos:", medias)

if __name__ == "__main__":
    main()
