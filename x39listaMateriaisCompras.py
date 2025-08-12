from typing import Tuple

listagem = ('Lápis', 1.75,
            'Borracha', 1,
            'Caderno', 6.50,
            'Estojo', 7.50,
            'Canetas', 4,
            'Mochila', 20,
            'apontador', 1.50,
            'livro', 5)
print('-'*30)
print(f'{"LISTAGEM DE PREÇOS":^40}')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:<10}')
