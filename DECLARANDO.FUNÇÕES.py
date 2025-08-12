def soma(a, b):
    s = a + b
    return s


def multiplica(a, b):
    m = a * b
    return m


def soma_multiplica(a, b):
    s = soma(a, b)
    m = multiplica(a, b)
    return print('Soma = ' + str(s) + ', Multiplica = ' + str(m))


soma_multiplica(5, 3)
