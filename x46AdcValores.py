números = list()
while True:
    n = int(input('Digite um valor:'))
    if n not in números:
        números.append(n)
        print('valor adicionado com sucesso.')
    else:
        print('valor duplicado!...')
    r = str(input('Quer continuar[S/N]'))
    if r in 'Nn':
        break
print('-'*30)
números.sort()
print(f'Você digitou os valores {números}')
