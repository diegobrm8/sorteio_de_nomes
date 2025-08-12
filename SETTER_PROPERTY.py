class ContaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError('Saldo não pode ser negativo!')
        self._saldo = valor


conta = ContaBancaria(1000)
print(conta.saldo)
conta.saldo = 2000
print(conta.saldo)
# conta.saldo = -1
print(conta.saldo)

print('-=' * 40)


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if len(valor) < 3:
            raise ValueError('Nome deve ter min 3 caracteres')
        self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor < 0 or valor > 120:
            raise ValueError('idade inválida')
        self._idade = valor


pessoa = Pessoa('Mary', 30)
print(pessoa.nome)
print(pessoa.idade)
print()
pessoa.nome = 'Maria'
pessoa.idade = 44
print(pessoa.nome)
print(pessoa.idade)
# pessoa.nome = 'lu'
# print(pessoa.nome)
