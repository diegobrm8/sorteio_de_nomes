from random import randint
from time import sleep


def sorteia_numeros(qtd_numeros):
    numeros = []
    while len(numeros) < qtd_numeros:
        num = randint(1, 60)
        if num not in numeros:
            numeros.append(num)
    numeros.sort()
    return numeros


def faz_jogos(qtd_jogos, qtd_numeros):
    jogos = []
    for i in range(qtd_jogos):
        numeros = sorteia_numeros(qtd_numeros)
        jogos.append(numeros)
    return jogos


print('-=' * 30)
print('JOGOS MEGA SENA')
print('-=' * 30)

quant = int(input('Quantos jogos quer que eu sorteie? '))
jogos = faz_jogos(quant, 6)

print(f'\nAqui estão seus {quant} jogos:\n')
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 3, 'BOA SORTE!', '-=' * 3)
