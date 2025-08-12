total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('nome do produto:'))
    preço = float(input('preço do produto: R$'))
    cont += 1
    barato = produto
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('''FIM DO PROGRAMA!''')
print(f'O total da compra foi {total}.')
print(f' Temos {totmil} produtos custando mais de mil reais')
print(f'O produto mais barato foi {barato}, que custa {menor}R$')
