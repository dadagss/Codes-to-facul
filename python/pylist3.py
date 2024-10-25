def contagem_caracteres(palavras):
    contagens = []
    for palavra in palavras:
        contagens.append(len(palavra))
    return contagens

lista_palavras = ['gato', 'cachorro', 'elefante', 'pássaro']
contagens = contagem_caracteres(lista_palavras)

for i, palavra in enumerate(lista_palavras):
    print(f'A palavra "{palavra}" tem {contagens[i]} caracteres.')
