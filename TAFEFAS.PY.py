from time import sleep

print('CHECKLIST')
lista_tarefas = []


def adicionar_tarefa(tarefa):
    lista_tarefas.append(tarefa)
    print(f'Tarrefa adicionada com sucesso!')


def mostrar_tarefas():
    if not lista_tarefas:
        print('Nenhuma tarefa a mostrar')
    else:
        for i, tarefa in enumerate(lista_tarefas):
            print(f'{i + 1}, {tarefa}')


def riscar_tarefa():
    if not lista_tarefas:
        print('\033[31mNão há tarefas para mostrar\033[m')
    else:
        num_tarefa = int(input('\033[32mdigite o número da tarefa que queira marcar\033[m: '))
        if num_tarefa <= len(lista_tarefas):
            tarefa_excluida = lista_tarefas.pop(num_tarefa - 1)
            print(f'Tarefa {num_tarefa} marcada como concluída.')
            return tarefa_excluida
        else:
            print('Número de tarefa inválido.')


while True:
    print('Escolha uma opção:')
    print('1. Adicionar tarefa')
    print('2. Mostrar todas as tarefas')
    print('3. Marcar tarefa como concluída')
    print('4. Sair do programa')

    escolha = input('\33[32mEscolha a opção desejada\033[m: ')
    if escolha == '1':
        tarefa = input('Que tarefa você quer adicionar? ')
        adicionar_tarefa(tarefa)
    elif escolha == '2':
        mostrar_tarefas()
    elif escolha == '3':
        riscar_tarefa()
    elif escolha == '4':
        print('\033[34mSaindo do programa\033[m...')
        sleep(1)
        break
    else:
        print('\033[mOpção inválida. Tente novamente\033[m.')

    sleep(1)
