def escreva(msg):
    tam = len(msg) + 2
    print('-=' * tam)
    print(f' {msg}')
    print('-=' * tam)


escreva('Diego Brum')
escreva('curso python')
escreva('Grêmio')
print("-=" * 40)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
