matriz = [[0, 0, 0, ], [0, 0, 0], [0, 0, 0]]
somapar = maior = somcol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite um valor para [{l},{c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('-=' * 30)

print(f'a soma dos pares é de {somapar}')
for l in range(0, 3):
    somcol += matriz[l][2]
print(f'a soma da terceira coluna é {somcol}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'o maior valor da segunda linha é {maior}')

