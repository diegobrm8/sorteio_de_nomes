nome = 'Diego Brum Azevedo'
print(nome.upper())
print(nome.lower())
dividido = nome.split()
print(dividido)
nomecompleto = ''.join(dividido)
print(nomecompleto)
print(f'Seu nome tem ao todo {len(nomecompleto)} caracteres e seu primeiro nome tem {(len(dividido[0]))} caracteres')

valores = []
for i in range(1, 10):
    if i % 2 == 0:
        valores.append(i)

valores1 = []
for i in range(2, 10, 2):
    valores.append(i)

valores2 = []
for i in range(1, 10):
    valores.append(i+1)

valores3 = []
for i in range(1, 10, 2):
    valores.append(i)

valores4 = []
for i in range(0, 10, 2):
    valores.append(i)

print(valores1)
print(valores2)
print(valores3)
print(valores4)
print(valores)