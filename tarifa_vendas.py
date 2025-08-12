class Loja:
    tarifa = 1.40

    def __init__(self, endereco: str) -> None:
        self._endereco = endereco

    def apresentar_endereco(self) -> None:
        print(self._endereco)

    @classmethod
    def vender(cls):
        return 40 * cls.tarifa

    @classmethod
    def alterar_tarifa(cls, nova_tarifa: int) -> None:
        cls.tarifa = nova_tarifa


lojapraia = Loja('praia')
lojacentro = Loja('centro')
lojapraia.apresentar_endereco()
lojacentro.apresentar_endereco()

print(lojacentro.vender())
print(lojapraia.vender())

lojacentro.alterar_tarifa(1.60)
print(lojacentro.vender())
