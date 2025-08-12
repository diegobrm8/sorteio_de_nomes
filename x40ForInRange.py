for c in range(0, 11):
    print(c)
print('''---''')
for c in range(0, 21, 2):
    print(c)

n = int(input('digite um número:'))
for c in range(0, n):
    print(c)


i = int(input('Início'))
f = int(input('Final'))
p = int(input('passo'))
for c in range(i, f+1, p):
    print(c)
