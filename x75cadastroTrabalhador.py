from datetime import datetime

dados = dict()

dados['nome'] = str(input('digite seu nome: '))
anonasci = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - anonasci
dados['ctps'] = int(input('Carteira de trabalho: (0 se não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('ano de contratação: '))
    dados['salario'] = float(input('digite o salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f'{k} tem o valor {v} ')