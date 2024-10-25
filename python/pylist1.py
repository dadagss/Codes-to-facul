
def criarlist(list):
    x = int
    while x != -1:
        x = int(input("Digite o valor de X (digite -1 para sair): "))
        list.append(x)
        continue

def somarlist(list):
    soma = 0
    for i in list:
        soma += i
    return soma + 1

def main():
    list = []
    soma = 0
    criarlist(list)
    soma = somarlist(list)
    print(f'a soma dos elementos da lista é {soma}')

if __name__ == "__main__":
    main()