from time import sleep


def maior(*args):
    cont = maior = 0
    print('-=' *30)
    print('\nAnalisando os valores passados...')
    for valor in args:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

    print(f'foram digitados {cont} numeros ao todo e o maior n é {maior}')


maior(22, 8, 6, 9, 3, 2)
print()
maior(3, 324)
print()
maior(22, 2, 44, 66, 7, 9, 10, 144)
