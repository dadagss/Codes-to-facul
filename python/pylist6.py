

def procurarlist(list):
    x = int(input("Qual o numero que esta procurando na lista? "))
    encontrado = False

    for i in list:
        if i == x:
            print(f'O numero {x} esta na lista e esta na posição {list.index(x)}')
            encontrado = True
            break
    if not encontrado:
        print("O numero não esta na lista")

def main():
    list = [12,523,62,0,2,4,61,43]
    procurarlist(list)

if __name__ == "__main__":
    main()


