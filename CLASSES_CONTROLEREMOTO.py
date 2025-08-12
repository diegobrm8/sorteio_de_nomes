class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura


controle_remoto = ControleRemoto('amarelo', '30cm', '10cm', '25')

controle_remoto2 = ControleRemoto('preto', '43cm', '15cm', '30')
print(controle_remoto.cor)
print(controle_remoto2.altura)
