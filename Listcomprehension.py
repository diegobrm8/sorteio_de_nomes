l3 = list(range(100))
ex1 = [v for v in l3 if v % 2 == 0 if v % 8 == 0]
print(ex1)

ex7 = [v if v % 5 == 0 else "não é" for v in l3]
print(ex7)

nomes = ['Ana', 'Bruno', 'Carla', 'Daniela', 'Eduardo', 'Felipe']
letra = 'C'
filtrados = list(filter(lambda x: x.startswith(letra), nomes))
print(filtrados)

letra2 = 'D'
filtredis = list(filter(lambda x: x.startswith(letra2), nomes))
print(filtredis)

letra3 = 'B'
outraletra = list(filter(lambda x: x.startswith(letra3), nomes))
print(outraletra)

maisdecinco = list(filter(lambda x: len(x) > 5, nomes))
print(maisdecinco)
