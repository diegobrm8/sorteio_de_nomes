def area(larg, comp):
    a = larg * comp
    print(f'a area de um terreno é de {a}m2')


print('CONTROLE DE TERRENOS.')
print('-=' * 30)
l = float(input('qual a largura? '))
c = float(input('qual a area? '))
area(l, c)
