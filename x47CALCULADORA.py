val1 = (int(input('digite um número')))
val2 = (int(input('digite outro número')))
opção = 0
while opção != 6:
    print('''Escolha uma das opções abaixo:                                                 
    [ 1 ] somar                                                                             
    [ 2 ] multiplicar                                                                       
    [ 3 ] subtrair                                                                          
    [ 4 ] o maior valor                                                                     
    [ 5 ] novos números                                                                     
    [ 6 ] sair do programa''')
    opção = int(input('Opções:'))
    if opção == 1:
        soma = val1 + val2
        print(f'{val1} + {val2} ={val1 + val2}')
    elif opção == 2:
        soma = val1 * val2
        print(f'{val1} * {val2} = {val1 * val2}')
    elif opção == 3:
        soma = val1 - val2
        print(f'{val1} - {val2} = {val1 - val2}')
    elif opção == 4:
        if val1 > val2:
            maior = val1
        else:
            maior = val2
            print(f'Entre {val1} e {val2} o maior valor é {maior}.')

    elif opção == 5:
        print('Informe os números novamente:')
        val1 = int(input('digite um número:'))
        val2 = int(input('digite outro número'))
    elif opção == 6:
        print('FINALIZANDO...')
