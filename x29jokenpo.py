import random
from random import randint
from time import sleep
itens = ["pedra", "papel", "tesoura"]
cpu = random.choice(itens)
jogador = 0
while jogador not in itens:
    jogador = input('pedra, papel ou tesoura? ')
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

if jogador == cpu:
    print(f'cpu escolheu {cpu} e jogador escolheu {jogador}, \033[33mEmpate!')

elif jogador == 'pedra':
    if cpu == 'papel':
        print(f'cpu escolheu {cpu} e jogador escolheu {jogador}, \033[31mVocê perdeu!')
    if cpu == 'tesoura':
        print(f'cpu escolheu {cpu} e jogador escolheu {jogador}, \033[32mVocê ganhou!')

elif jogador == 'tesoura':
    if cpu == 'pedra':
        print(f'cpu escolheu {cpu} e jogador escolheu {jogador},\033[31mVocê perdeu!')
    if cpu == "papel":
        print(f'cpu escolheu {cpu} e jogador escolheu {jogador},\033[32mVocê ganhou!')

elif jogador == "papel":
    if cpu == 'tesoura':
        print(f'cpu escolheu {cpu} e jogador escolheu {jogador},\033[31mVocê perdeu!')
    if cpu == 'pedra':
        print(f'cpu escolheu {cpu} e jogador escolheu {jogador},\033[32mVocê ganhou!')






