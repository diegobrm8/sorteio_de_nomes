print('''SEJA BEM VINDO AO JOGO DE PERGUNTAS E RESPOSTAS!''')
acertos: int = 0
erros: int = 0

pergunta1 = str(input('Qual o melhor time do mundo?'))
if pergunta1 == 'Grêmio':
    print('\033[32mACERTOU\033[m')
    acertos += 1
else:
    print('\033[31mVOCE ERROU\033[m')
    erros += 1


pergunta2 = str(input('Celso Portiolli tem haver com o 11 de Setembro ?'))
if pergunta2 == 'sim':
    acertos += 1
    print('\033[32mACERTOU\033[m!')
else:
    erros += 1
    print('\033[31VOCE ERROU\033[m')


pergunta3 = str(input('Qual maior osso do corpo humano?'))
if pergunta3 == 'fêmur':
    acertos += 1
    print('\033[32mACERTOU\033[m')
else:
    erros += 1
    print('\033[31mVOCE ERROU\033[m')


pergunta4 = str(input('Em que ano o homem pisou na lua?'))
if pergunta4 == '1969':
    acertos += 1
    print('\033[32mACERTOU!\033[m')
else:
    erros += 1
    print('\033[31mVOCE ERROU\033[m')


pergunta5 = str(input('Qual a capital do RS?'))
if pergunta5 == 'Porto Alegre':
    acertos += 1
    print('\033[32mACERTOU!\033[m')
else:
    erros += 1
    print('\033[31VOCÊ ERROU\033[m')

print(f'você teve {acertos} acertos e {erros} erros!')
