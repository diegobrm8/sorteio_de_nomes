aluno = dict()  # ou{}
aluno['nome'] = str(input('nome: '))
aluno['média'] = float(input(f'média de {aluno["nome"]}:'))
if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'{k} é {v}')