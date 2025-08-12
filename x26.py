n = int(input('digite seu número:'))
c = int(input('voce deseja converter esse número para que?:\n1 - para binário: \n2 - para octal:\n3 - para hexadecimal:'))

if c == 1:
    print(f' {bin(n)}')
elif c == 2:
    print(f'{oct(n)}')
elif c == 3:
    print(f'{hex(n)}')
else:
    print('escolha uma opção válida!')

n1 = int(input('digite um número:'))
n2 = int(input('digite outro número:'))
if n1 > n2:
    print(f'O maior valor é {n1}')
if n1 < n2:
    print(f'O maior valor é {n2}')
if n1 == n2:
    print('os valores são iguais não há um valor maior nem menor')


ano = int(input('digite sua data de nascimento:'))
if ano < 2004:
    print('voce tem mais de 18 anos está na hora de se alistar')
if ano >= 2004:
    print('voce não tem mais de 18 anos, ainda não pode se alistar')

n1 = float(input('digite sua nota:'))
n2 = float(input('digite sua outra nota:'))
m = (n1+n2)/2
if m >= 7:
    print(f'Sua média é {m} e você foi aprovado!')
else:
    print(f'Sua média é {m} e você foi reprovado!')











