class Despesa:
    def __init__(self, descricao, categoria, valor):
        self.descricao = descricao
        self.categoria = categoria
        self.valor = valor


class ControleDespesas:
    def __init__(self):
        self.despesas = []

    def adicionar_despesas(self, despesas):
        self.despesas.append(despesas)

    def lista_despesas(self):
        if self.despesas:
            for index, despesa in enumerate(self.despesas, start=1):
                print(f'{index}.Descricao: {despesa.descricao}')
                print(f'categoria: {despesa.categoria}')
                print(f'Valor: R${despesa.valor}')

        else:
            print('\033[31mNenhuma despesa foi cadastrada\033[0m')


if __name__ == '__main__':
    controle = ControleDespesas()

    while True:
        print('1. Adicionar Despesas')
        print('2. Listar Despesas')
        print('3. Sair')
        opcao = input('escolha uma opcao:')

        if opcao == '1':
            descricao = input('Qual a descricao do produto?')
            categoria = input('Qual a categoria do produto?')
            valor = input('Qual o valor do produto?')
            despesa = Despesa(descricao, categoria, valor)
            controle.adicionar_despesas(despesa)
            print('-' * 30)
            print('\033[32mDespesa adicionada com sucesso!\033[0m')
            print('-' * 30)

        elif opcao == '2':
            print('Lista de produto: ')
            controle.lista_despesas()

        elif opcao == '3':
            print('\033[32mFinalizando...\033[0m')
            break


        else:
            print('\033[31mOpção invalida, tente novamente!\033[0m')
