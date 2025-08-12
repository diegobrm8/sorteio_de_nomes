# STYLE:0-NONE,1-bold,4-underline,7-negative
# texto
# 30  branco
# 31  vermelho
# 32  verde
# 33  amarelo
# 34  azul
# 35  roxo
# 36  ciano
# 37  cinza
# fundo:
# 40-branco,41-vermelho,42-verde,43-amarelo,44-azul,45-roxo,46-ciano,47-cinza
print('\033[7;31;47mSalveee.\033[m')
print('\033[31;40mERRO!digiteblablabla')
print('\033[1;31;46mOlámundovki!\033[m')
print('\033[4;31;47mOlá mundo!\033[m')
print('\033[35mteste')
print('\033[31mGAME OVER\033[m')
print('\033[31;43mOlá mundo\033[m')
print('\033[32mOlá mundo\033[m')
print('\033[0;31mred\033[m')
print('\033[32;43mseila\033[m')


def x(n):
    if n >= 0 and n <= 2:
        return n
    else:
        return x(n-1) + x(n-2) + x(n-3)

print(x(6))