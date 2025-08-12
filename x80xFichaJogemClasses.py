class Jogador:
    def __init__(self, nome, gols, partidas):
        self.nome = nome
        self.gols = gols
        self.partidas = partidas

    def apresentar(self):
        print(f"O jogador {self.nome} fez {self.gols} gols em {self.partidas} partidas.")


jogador1 = Jogador('Marquin', 22, 15)
jogador1.apresentar()
jogador2 = Jogador('Junin', 13, 15)
jogador2.apresentar()
jogador3 = Jogador('Marcelin', 12, 14)
jogador3.apresentar()
