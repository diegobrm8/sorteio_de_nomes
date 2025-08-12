valores = []

while True:

    valor = int(input('Digite um valor: '))

    valores.append(valor)

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()

    if continuar == 'S':

        print('Vamos continuar!')

    if continuar == 'N':

        break

print('-='*30)
print(f'você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'os valores em ordem decrescente são {valores}')
