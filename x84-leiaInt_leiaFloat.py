def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor digite um número inteiro valido.\033[m')
            continue
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor digite um número inteiro valido.\033[m')
            continue
        else:
            return n


num = leiaint('digite um valor: ')
num2 = leiafloat('digite outro')
print(f'o valor digitado foi {num} e o real {num2}')
