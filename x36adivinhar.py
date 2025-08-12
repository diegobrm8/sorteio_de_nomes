from random import randint

cpu = randint(0, 10)
print('Sou seu computador... Acabei de pensar em número entre 0 e 10, vamos ver se você adivinha qual foi: ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    palpites += 1
    if jogador == cpu:
        acertou = True
    else:
        if jogador < cpu:
            print('mais,tenta de novo')
        elif jogador > cpu:
            print('menos, tenta de novo')
if palpites < 4:
    print(f'acertou com {palpites} tentativas.PARABÉNS')
elif palpites >= 4:
    print(f'ALELUIA, acertou com {palpites} tentativas, até que enfim jaguara')
