soma = cont = 0
while True:
    num = int(input('digite um valor para parar:'))
    if num == 999:
        break
    cont += 1
    soma += num
print(''''ACABOU!''')
print(f'Foram digitados {cont} valores, e a soma dos valores foi {soma}')
