import enum


class Estado(enum.Enum):
    ININICIADO = 'iniciado'
    EM_ANDAMENTO = 'em andamento'
    PAUSADO = 'pausado'
    FINALIZADO = 'finalizado'


class Tarefa:
    def __init__(self, nome, estado):
        self.nome = nome
        if isinstance(estado, Estado):
            self.estado = estado
        else:
            raise ValueError('estado invalido')

    def alterar_estado(self, novo_estado):
        if isinstance(novo_estado, Estado):
            self.estado = novo_estado
        else:
            raise ValueError('Estado inválido')

    def __str__(self):
        return f'Tarefa: {self.nome}, Estado: {self.estado}'
