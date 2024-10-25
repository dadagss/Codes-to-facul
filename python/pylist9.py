def manipular_strings(lst):
    # Inverter cada string da lista
    strings_invertidas = [s[::-1] for s in lst]
    
    # Contar o número total de caracteres após a inversão
    total_caracteres = sum(len(s) for s in strings_invertidas)
    
    return strings_invertidas, total_caracteres

def main():
    # Exemplo de lista de strings
    lst = ["casa", "carro", "python", "exemplo"]
    
    # Chama a função e imprime os resultados
    strings_invertidas, total_caracteres = manipular_strings(lst)
    
    print("Strings invertidas:", strings_invertidas)
    print("Total de caracteres:", total_caracteres)

if __name__ == "__main__":
    main()
