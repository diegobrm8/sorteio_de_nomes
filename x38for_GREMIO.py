lanche = ('hamburguer', 'Suco', 'Pizza', 'batata frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('''Grêmio''')

Grêmio = ['Brenno', 'Edilson', 'Geromel', 'Kanneman', 'Nicolas', 'Villasanti', 'L.Silva', 'Bitello', 'Cristaldo', 'Elias', 'D.Sousa']
Grêmio.remove("Elias")
Grêmio.remove("L.Silva")
Grêmio.insert(6, "Lucas Leiva")
Grêmio.insert(9, "Ferreira")
Grêmio.remove('Nicolas')
Grêmio.remove('Edilson')
Grêmio.remove('D.Sousa')
Grêmio.insert(1, 'Fabio')
Grêmio.insert(4, 'Reinaldo')
Grêmio.insert(12, 'Luiz Suarez')
Grêmio.remove('Lucas Leiva')
Grêmio.insert(6, 'Pepê')
print('\033[32mManeira1\033[m!')


for cont in range(0, len(Grêmio)):
    print(f'{Grêmio[cont]}')
print('\033[32mManeira2\033[m!')
for time in Grêmio:
    print(f'{time}')
