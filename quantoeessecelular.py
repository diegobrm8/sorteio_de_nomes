while True:
    produto = str(input('nome do produto: '))
    preço = float(input('Preço: R$'))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break


