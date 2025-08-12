ficha = list()
aprovados = 0
while True:
    aluno = str(input('digite o nome do aluno: '))
    nota1 = float(input('digite uma nota: '))
    nota2 = float(input('digite uma nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([aluno, [nota1, nota2], media])
    resp = str(input('quer continuar? [S/N]'))
    if resp in 'nN':
        break
    if media >= 6:
        aprovados += 1


print('-=' * 30)
print(f'{"N.":^4}{"NOME":^10}{"MEDIA":^8}')
for i, a in enumerate(ficha):
    print(f'{i+1:^4} {a[0]:^10} {a[2]:^8}')

aprovados = list(filter(lambda x: x[2] >= 6, ficha))
print()
print('alunos aprovados')
for aluno in aprovados:
    print(aluno[0])
    