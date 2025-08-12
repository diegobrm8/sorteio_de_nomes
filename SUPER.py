class Animal:
    def fazer_som(self):
        print('O animal faz um som')


class Cachorro(Animal):
    def fazer_som(self):
        super().fazer_som()
        print('O cachorro late')


cachorro = Cachorro()
cachorro.fazer_som()

print('-=' * 30)


class Veiculo:
    def __init__(self, cor):
        self.cor = cor


class Carro(Veiculo):
    def __init__(self, cor, marca):
        super().__init__(cor)
        self.marca = marca

    def detalhes(self):
        print(f'Este carro é da marca {self.marca} e tem a cor super {self.cor}.')


carro = Carro('vermelho', 'Toyota')
carro.detalhes()
print('-=' * 30)


class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Estudante(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)
        self.curso = curso

    def apresentar(self):
        print(f"Olá, eu sou {self.nome} e estou estudando {self.curso}.")


estudante = Estudante('Diego', 'Python')
estudante.apresentar()
