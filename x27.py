nascimento = int(input('digite sua data de nascimento:'))
idade = 2022 - nascimento
if idade <= 9:
    print('mirim')
elif idade <= 14:
    print('infantil')
elif idade <= 19:
    print('júnior')
elif idade <= 20:
    print('sênior')
elif idade > 20:
    print('master')


peso = int(input('digite seu peso:'))
altura = float(input('digite sua altura:'))
imc = peso/(altura*altura)
print(f'seu imc é {imc}')
if imc < 18.5:
    print(float('abaixo do peso:'))
elif 18.5 <= imc < 25:
    print('peso ideal')
elif 25 <= imc < 38:
    print('acima do peso')
elif imc >= 38:
    print('baleia')













