from time import sleep
c = ('\033[m',  # 0 - sem cores
     '\033[0;30;41m',  # 1 - fundo vermelho
     '\033[0;30;42m',  # 2 - fundo verde
     '\033[0;30;43m',  # 3 - fundo amarelo
     '\033[0;30;44m',  # 4  - fundo azul
     '\033[0;30;45m',  # 5 - fundo roxo,
     '\033[300m',  # 6 - branco
     '\033[0;31m',  # 7 - vermelho
     '\033[0;32m',  # 8 - verde
     '\033[0;33m',  # 9 - amarelo
     '\033[0;34m',  # 10 - azul
     '\033[0;35m',  # 11 - roxo
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP!', 6)
    comando = str(input('Função ou biblioteca >>  :'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 3)
