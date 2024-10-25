#verificando quantas vogais há no codigo
x = "banana"


count = 0
vogais = "aeiouAEIOU"
for caractere in x:
    if caractere in vogais:
        count += 1

print(count)