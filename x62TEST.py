def cria_matriz(num_lin, num_col):
    matriz = []
    for i in range(num_lin):
        linha = []
        for j in range(num_col):
            valor = int(input('digite o elemento[' + str(i) + '][' + str(j) + ']'))
            linha.append(valor)
        matriz.append(linha)

    return matriz


def lematriz():
    lin = int(input('digite o numero de linhas: '))
    col = int(input('digite o numero de colunas: '))
    return cria_matriz(lin, col)


m = lematriz()
print()
palavra = "Python"

print( palavra[3])

print(palavra[1])

print(palavra[-2])

print( palavra[0])

print(palavra[-1])

print(palavra[4])