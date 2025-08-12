r1 = float(input('quantos reais você tem na carteira? R$'))
d = r1 / 5.10
e = r1 / 6.25

print(f'você tem R${r1} na carteira e pode comprar {d.__round__(2)} doláres ou {e} euros')
