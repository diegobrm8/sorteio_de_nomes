class CaixaBanco:
    def __init__(self):
        self.cedulas = {
            100: 0,
            50: 0,
            20: 0,
            1: 0
        }

    def depositar(self, valor):
        for cedula in sorted(self.cedulas.keys(), reverse=True):
            quantidade_celulas = valor // cedula
            self.cedulas[cedula] += quantidade_celulas
            valor -= quantidade_celulas * cedula

    def sacar(self, valor):
        if valor > self.consultar_saldo():
            print('Saldo insuficiente')

        for cedula in sorted(self.cedulas.keys(), reverse=True):
            quantidade_cedulas = min(valor // cedula, self.cedulas[cedula])
            self.cedulas[cedula] -= quantidade_cedulas
            valor -= quantidade_cedulas * cedula

            print('Saque realizado com sucesso!')

    def consultar_saldo(self):
        saldo = 0
        for cedula, quantidade in self.cedulas.items():
            saldo += cedula * quantidade
        return saldo


caixa = CaixaBanco()

print('Saldo atual', caixa.consultar_saldo())
caixa.depositar(350)
print("Saldo atual:", caixa.consultar_saldo())
