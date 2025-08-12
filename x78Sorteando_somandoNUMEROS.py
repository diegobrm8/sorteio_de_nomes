from random import randint


def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ')


def soma_par(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'somando os valores pares de {lista} temos {soma} ')


numeros = list()
sorteia(numeros)
soma_par(numeros)
print('-=' * 30)
soma_dosNPAR = lambda lista: sum(filter(lambda x: x % 2 == 0, lista))
resultado = soma_dosNPAR(numeros)
print(resultado)
