def cadastrar_pessoas():
    galera = []
    while True:
        pessoa = {"nome": str(input('Digite seu nome: '))}
        while True:
            pessoa["sexo"] = str(input('Sexo: [M/F]')).upper()
            if pessoa["sexo"] in 'MF':
                break
            print('\033[31mERRO! Por favor, digite M ou F:\033[m')
        pessoa["idade"] = int(input('Digite sua idade: '))
        galera.append(pessoa.copy())
        while True:
            resp = str(input('Quer continuar? [S/N]?')).upper()
            if resp in 'SN':
                break
        if resp == 'N':
            break
    return galera


def exibir_estatisticas(galera):
    soma = media = 0
    masc = fem = 0
    for pessoa in galera:
        soma += pessoa["idade"]
        if pessoa["sexo"] == "M":
            masc += 1
        else:
            fem += 1
    media = soma / len(galera)
    print('-=' * 30)
    print(f'Foram cadastradas {len(galera)} pessoas')
    print(f'A média de idade é de {media:.2f} anos')
    print(f'Foram cadastrados {masc} homens e {fem} mulheres')


galera = cadastrar_pessoas()
exibir_estatisticas(galera)

