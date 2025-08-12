soma = 0
for mult in range(1, 501, 3):
    if mult % 2 != 0:
        soma += mult
print(soma)

n = int(input('DIGITE UM NÚMERO: '))
print(f'a tabuada do número {n} é:')
n1 = 0
x = 0
for c in range(10):
    x = x + 1
    n1 = n1 + n
    print(f'{n} x {x} = {n1}')


s = 0
for c in range(1, 7):
    n = int(input(f"Digite o {c}º número a ser considerado:"))

    if n % 2 == 0:
        s += n
print(f'A soma dos pares que você digitou é: {s}')
