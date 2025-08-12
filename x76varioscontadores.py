from time import sleep


def contador(i, f, p):
    print(f'contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=False)
            sleep(0.5)
            cont += p
        print('\033[32mFIM!\033[m')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=False)
            sleep(0.5)
            cont -= p
        print('\033[31mFIM!\033[m')


contador(1, 10, 2)
contador(10, 0, 1)
contador(100, 0, 10)
print('Agora personalize a contagem: ')
ini = (int(input('Inicio: ')))
final = (int(input('final: ')))
passo = (int(input('passo: ')))
contador(ini, final, passo)