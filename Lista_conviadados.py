lista_convidados = []

while True:
    print("1- Adicionar nome")
    print("2- Verificar nome")
    print("3- Exibir Lista")
    print("4- Remover nome")
    print("0- Sair")
    opcão = int(input('escolha uma opção [0-4]: '))

    if opcão == 0:
        break
    if opcão == 1:
        nome = input('Digite o nome do convidado: ')
        if nome in lista_convidados:
            print(f'{nome} já esta na lista!')
        else:
            lista_convidados.append(nome)
            print(f'{nome} adicionado a lista! ')
    if opcão == 2:
        nome = input('digite o nome que queira verificar: ')
        if nome in lista_convidados:
            print(f'{nome} está na lista.')
        else:
            print(f'{nome} não está na lista.')
    if opcão == 3:
        lista_convidados.sort()
        print('LISTA DE CONVIDADOS: ')
        numero = 1
        for nomes in lista_convidados:
            print(f'{numero}: {nomes.upper()}')
            numero += 1
    if opcão == 4:
        nome = input('Digite o nome que queira remover:')
        if nome in lista_convidados:
            lista_convidados.remove(nome)
            print(f'{nome} foi removido')
        else:
            print(f'{nome} não estava na lista:')
