num = list()
pares = list()
impar = list()
while True:
    num.append(int(input('Digite um numero: ')))
    res = str(input('Quer continuar? s ou n? '))
    if res in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impar.append(v)

print('=-' * 30)
print(f' são {len(num)} números na lista')
print(f'os pares são {pares}')
print(f'os impares são {impar}')
