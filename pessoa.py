class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo {alimento}')
            return

        print(f'{self.nome}  está comendo {alimento}')
        self.comendo = True

    def para_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} já está falando')
            return

        print(f'{self.nome} esta falando sobre {assunto}')
        self.falando = True

    def esfaquear(self):
        print(f'{self.nome} foi esfaqueada')
    def morrer(self):
        print(f'{self.nome} está morrendo')
