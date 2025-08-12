from random import randint

cpu = randint(0, 5)
jogador = int(input('escolha um número de 1 a 5:'))
print(f'pensei no número {cpu}')
if cpu == jogador:
    print('''PARABÉNS VOCÊ GANHOU!''')
else:
    print('VOCÊ PERDEU')




