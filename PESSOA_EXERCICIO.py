class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def aumentaIdade(self, idade):
        self.idade += 1
        return self.idade

    def aumentaPeso(self, peso):
        self.peso += 10
        return self.peso

    def aumentaTamanho(self, altura):
        self.altura += 0.05
        return self.altura


p1 = Pessoa('João', idade=40, peso=75, altura=1.82)
p2 = Pessoa('Marcelo', idade=34, peso=68, altura=1.73)
print(p1.aumentaPeso(peso=None))
print(p1.aumentaTamanho(altura=None))
print(p2.aumentaTamanho(altura=None))
print(p2.aumentaIdade(idade=None))
print(p2.aumentaIdade(idade=38))
print(p2.aumentaIdade(idade=38))
print(p2.aumentaIdade(idade=38))
print(p1.idade)
print(p2.idade)