quantidade = int(input('quantidade de alunos[1-200]: '))
while quantidade < 1 and quantidade > 200:
    quantidade = int(input('Opção invalida! digite novamente[1-200]:'))
aprovados = 0
reprovados = 0
i = 0
while i < quantidade:
    nota1 = float(input('digite nota1: '))
    nota2 = float(input('digite nota2: '))
    nota3 = float(input('digite nota3: '))
    nota4 = float(input('digite nota4: '))
    while nota1 < 0 and nota1 > 0 or 0 > nota2 > 10:
        nota1 = float(input('Opção inválida! digite novamente[0-10]: '))
        nota2 = float(input('Opção inválida! digite novamente[0-10]: '))
    média = (nota1 + nota2 + nota3 + nota4) / 4
    print(f'Média do aluno: {média}')
    if média >= 6:
        aprovados += 1
    else:
        reprovados += 1
    i += 1
print(f'Foram {aprovados} alunos aprovados e {reprovados} alunos reprovados.')