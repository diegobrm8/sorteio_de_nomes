largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

for i in range(altura):
    linha = ''
    for j in range(largura):
        linha += '#'
    print(linha)
        