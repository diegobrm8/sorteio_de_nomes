from typing import Type


class Interruptor:
    def __init__(self, comodo):
        self.__comodo = comodo

    def acender(self):
        print(f'acendendo {self.__comodo}')

    def apagar(self):
        print(f'apagando {self.__comodo} ')


class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    def dormir(self):
        print('fui mimir')


Dieguito = Pessoa()
lhama = Pessoa()
interruptor_quarto = Interruptor('quarto')
interruptor_cozinha = Interruptor('Cozinha')
interruptor_sala = Interruptor('sala')
lhama.acender_luz(interruptor_quarto)
lhama.acender_luz(interruptor_cozinha)
lhama.apagar_luz(interruptor_sala)
Dieguito.dormir()
