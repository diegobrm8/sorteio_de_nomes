def leiaint():
    n = str(input('Digite um número: '))
    while not n.isnumeric():
        print('\033[0;31mERRO! digite um número válido\033[m!')
        n = str(input('Digite um número: '))

    if n.isnumeric():
        n = int(n)
        print(f'Você digitou o número: {n} ')


leiaint()


