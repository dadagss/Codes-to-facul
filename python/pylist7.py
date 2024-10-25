def verificarprimos(lst):
    primos = []
    Nprimos = []

    for num in lst:
        if num < 2:
            Nprimos.append(num)
        else:
            # Assume que o número é primo até provar o contrário
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    Nprimos.append(num)
                    is_prime = False
                    break
            if is_prime:
                primos.append(num)
    
    return primos, Nprimos

def main():
    lst = [12, 541, 15, 7, 61, 49, 3, 2, 17]
    primos, Nprimos = verificarprimos(lst)

    print("Primos:", primos)
    print("Não primos:", Nprimos)

if __name__ == "__main__":
    main()
