def transpor_matriz(matriz):
    # Cria a matriz transposta usando list comprehension
    matriz_transposta = [list(row) for row in zip(*matriz)]
    return matriz_transposta

def main():
    # Exemplo de matriz
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Chama a função para obter a matriz transposta
    matriz_transposta = transpor_matriz(matriz)
    
    # Imprime a matriz transposta
    print("Matriz Transposta:")
    for linha in matriz_transposta:
        print(linha)

if __name__ == "__main__":
    main()
