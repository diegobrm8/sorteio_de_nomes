a = [1, 2, 3, 4]
b = a
b[2] = 8
print(a)
print(b)

print('-' * 30)
print('''COPIA DE LISTA!''')

a = [1, 2, 3, 4]
b = a[:]
b[2] = 8
print(a)
print(b)

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))
