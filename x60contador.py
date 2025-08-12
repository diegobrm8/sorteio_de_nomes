def contador(i, f, p):
    c: object = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


# cont, final, passo
contador(0, 100, 10)
help(contador)
""
