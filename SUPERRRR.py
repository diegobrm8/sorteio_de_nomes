class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f'Pessoa: {self.nome}'


class Estudante(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula

    def __str__(self):
        return f'Estudante: {self.nome}, Matrícula: {self.matricula}'


pessoa = Pessoa('Joao')
print(pessoa)
estudante = Estudante('Maria', '12345')
print(estudante)
