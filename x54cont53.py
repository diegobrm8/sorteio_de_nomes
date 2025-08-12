estado = dict()
brasil = list()
tot = int(input('Quantos estados? '))
for c in range(0, tot):
    estado['uf'] = str(input('Unidade Federativa:'))
    estado['sigla'] = str(input('Sigla do estado:'))
    brasil.append(estado.copy())
print(brasil)
print('-=' * 30)
for e in brasil:
    print(e)
print('-=' * 30)



