class Pessoa:
    def __int__(self, nome):
        self.nome = nome

    def saudacao(self):
        return f'Olá eu sou {self.nome}'


class Estudante(Pessoa):
    def __init__(self, nome, instituicao):
        super().__int__(nome)
        self.instituicao = instituicao

    def saudacao(self):
        mensagem_pai = super().saudacao()
        return f"{mensagem_pai} Eu sou um estudante da {self.instituicao}."


estudante = Estudante('Joao', 'universidade XYZ')
print(estudante.saudacao())
