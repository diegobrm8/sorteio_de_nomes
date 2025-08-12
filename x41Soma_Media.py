soma = 0
média = 0
for c in range(0, 10):
    n = int(input('digite um número:'))
    soma += n
    média = soma / 10
print(f'a soma dos números foi de {soma}')
print(f'A média dos alunos foi de {média}')
