nome = str(input('digite seu nome:'))
sexo = str(input('informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados Inválidos,informe seu sexo:'))
print(f'sexo {sexo} registrado com sucesso')
































