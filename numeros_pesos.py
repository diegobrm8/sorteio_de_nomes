temp = []
tempprincip = []
maior = menor = 0

while True:
    temp.append(str(input('digite o nome: ')))
    temp.append(float(input('digite o peso: ')))
    if len(tempprincip) == 0:
        maior = menor = temp[1]

    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    tempprincip.append(temp[:])
    temp.clear()
    resp = input('Quer continuar? [sn]')

    if resp in 'Nn':
        break

print('-=' * 30)
print(f'Os dados foram {tempprincip}')
print(f'Ao todo foram {len(tempprincip)} pessoas')
print(f'o maior peso é de {maior} e o de menor peso é de {menor}')
