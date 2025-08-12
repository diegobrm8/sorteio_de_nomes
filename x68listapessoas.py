galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa["nome"] = str(input('digite seu nome: '))
    while True:
        pessoa["sexo"] = str(input('sexo: [M/F]')).upper()
        if pessoa["sexo"] in 'MF':
            break
        print('\033[31mERRO! por favor digite M ou F:\033[m')
    pessoa["idade"] = int(input('digite sua idade: '))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]?')).upper()
        if resp in 'S/N':
            break
    if resp == 'N':
        break

print('-=' * 30)
for k, v in enumerate(galera):
    print(k+1, v)
media = soma / len(galera)
print('-=' * 30)
print(f'ao todo foram {len(galera)} pessoas cadastradas')
print(f'A média de idade é de {media}')
masc = [pessoa["nome"] for pessoa in galera if pessoa["sexo"] == "M"]
fem = [pessoa["nome"] for pessoa in galera if pessoa["sexo"] == 'F']

print(f'As pessoas do sexo masculino são: {", ".join(masc)}')
print(f'As pessoas do sexo feminino são: {", ".join(fem)}')
