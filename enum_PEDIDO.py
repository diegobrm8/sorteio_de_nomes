import enum


class StatusPedido(enum.Enum):
    PENDENTE = 'Pendente'
    EM_ANDAMENTO = 'Em andamento'
    CONCLUIDO = 'Concluído'
    CANCELADO = 'Cancelado'


class Pedido:
    def __init__(self, numero, status):
        self.numero = numero
        if isinstance(status, StatusPedido):
            self.status = status
        else:
            ValueError('Status invalido')

    def alterar_status(self, novo_status):
        if isinstance(novo_status, StatusPedido):
            self.status = novo_status
        else:
            raise ValueError('Status inválido')

    def __str__(self):
        return f'Pedido #{self.numero}: {self.status.value}'


pedido1 = Pedido(1, StatusPedido.PENDENTE)
print(pedido1)  # Saída: Pedido #1: Pendente

pedido1.alterar_status(StatusPedido.EM_ANDAMENTO)
print(pedido1)  # Saída: Pedido #1: Em andamento

pedido2 = Pedido(2, 'Cancelado')
