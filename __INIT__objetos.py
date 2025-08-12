class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            print('\033[31mPlano inválido\33[m')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('\033[31mPlano inválido')


Cliente = Cliente('Diego', 'diego.azvd8@gmail.com', 'basico')
Cliente.mudar_plano('premium')
print(Cliente.plano)
