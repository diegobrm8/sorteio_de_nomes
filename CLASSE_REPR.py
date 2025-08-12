class Personagem:
    def __init__(self, nome, cor, tamanho):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho

    def __repr__(self):
        return f'Personagem("{self.nome}", "{self.cor}", "{self.tamanho}")'


mickey = Personagem('Mickey', 'Preto', '120cm')
pluto = Personagem('Pluto', 'laranja', '70cm')
print(mickey)
print(pluto)
