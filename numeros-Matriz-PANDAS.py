import pandas as pd

# Criando uma matriz com 3 linhas e 4 colunas
matriz = pd.DataFrame([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                      columns=['Coluna1', 'Coluna2', 'Coluna3', 'Coluna4'])

print(matriz)
print()
matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(matrix[1])
print(matrix[0])
print(matrix[2])
print()
for c in matrix:
    print(c)

print('-=' * 30)
matrix3 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
transposed = [[linha[i] for linha in matrix3] for i in range(len(matrix3[0]))]
for linha in transposed:
    print(linha)
