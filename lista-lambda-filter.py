numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Imprime [2, 4, 6, 8, 10]

impares = list(filter(lambda x: x % 2 != 0))
print(impares)

print()


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


pessoas = [Pessoa('Ana', 25), Pessoa('Bruno', 30), Pessoa('Carla', 20)]
idosos = list(filter(lambda x: x.idade >= 25, pessoas))
for pessoa in idosos:
    print(pessoa.nome)
jovens = list(filter(lambda x: x.idade < 20, pessoas))
print(jovens)
