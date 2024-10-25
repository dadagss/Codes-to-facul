def produto_matrizes(A, B):
    if len(A[0]) != len(B):
        raise ValueError("O número de colunas da matriz A deve ser igual ao número de linhas da matriz B.")

    resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Realiza a multiplicação de matrizes
    for i in range(len(A)):  
        for j in range(len(B[0])):  #
            for k in range(len(B)):  
                resultado[i][j] += A[i][k] * B[k][j]

    return resultado

A = [
    [1, 2],
    [3, 4],
    [5, 6]
]

B = [
    [7, 8, 9],
    [10, 11, 12]
]

resultado = produto_matrizes(A, B)

for linha in resultado:
    print(linha)
