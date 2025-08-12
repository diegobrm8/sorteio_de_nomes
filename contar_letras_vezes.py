frase = str(input('digite a frase para contar letras: '))
d = {}
for letra in frase:
    if letra in d:
        d[letra] = d[letra]+1
    else:
        d[letra] = 1
print(d)
