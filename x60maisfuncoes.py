def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'somando os valores {valores} temos {s}')


soma(5, 3)
soma(2, 9, 4)
print()
print('=-' * 30)
print()

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = (int(input('Digite um número:')))
if par(num):
    print('É par')
else:
    print('Não é par')
