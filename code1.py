import random

#codigo para verificar se numero e impar ou par
x = random.randint(1,100)

print(x)

if x % 2 == 0:
    print("Numero par")
else: 
    print("numero impar")