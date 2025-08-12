class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passa_canal(self, botão):
        if botão == "+":
            print('Aumentar o canal')
        elif botão == "-":
            print('diminuir o canal')


controle_remoto = ControleRemoto("preto", "10cm", "2cm", "2cm")
controle_remoto2 = ControleRemoto("cinza", "10cm", "2cm", "2cm")
print(controle_remoto2.cor)
controle_remoto2.passa_canal("+")
