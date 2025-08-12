perguntas = {
    'Pergunta 1': {
        'Pergunta': 'quanto é 2+2?',
        'respostas': {'a': '22', 'b': '4', 'c': '8', },
        'resposta_certa': 'b',
    },

    'Pergunta 2': {
        'Pergunta': 'Palmeiras tem mundial? ',
        'respostas': {'a': 'vários', 'b': 'sim, de 51', 'c': 'não', },
        'resposta_certa': 'c',
    },

    'Pergunta 3': {
        'Pergunta': 'Qual maior osso do corpo humano? ',
        'respostas': {'a': 'mão', 'b': 'Fêmur', 'c': 'Tíbia', },
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'Pergunta': 'De que país é o QOTSA ?',
        'respostas': {'a': 'Estados Unidos', 'b': 'Inglaterra', 'c': 'Suécia', },
        'resposta_certa': 'a',
    },

    'Pergunta 5': {
        'Pergunta': 'Qual capital do RS ?',
        'respostas': {'a': 'Viamão', 'b': 'Porto Alegre', 'c': 'Novo Hamburgo', },
        'resposta_certa': 'b',
    },
    'Pergunta 6': {
        'Pergunta': 'Qual a melhor ling de programação?',
        'respostas': {'a': 'java', 'b': 'python', 'c': 'Html', },
        'resposta_certa': 'b',

    },
}
print()

respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["Pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv["respostas"].items():
        print(f'[{rk}]: {rv}')
    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pv["resposta_certa"]:
        print('\033[32mPARABÉNS, VOCÊ ACERTOU\033[m')
        respostas_certas += 1
    else:
        print('\033[31mVISH,VOCÊ ERROU!\033[m')
    print()
qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'A porcentagem de acerto é de {porcentagem_acerto}%')