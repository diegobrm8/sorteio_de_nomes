valorcasa = float(input('Qual é o valor da casa?'))
valorsalario = float(input('Qual seu salário?'))
anospagamento = float(input('em quantos anos pretende pagar?'))

parcela = valorcasa/(anospagamento*12)

if parcela > (30/100)*valorsalario:
    print('empréstimo negado, motivo: parcela excedeu 30% de seu salário')
else:
    print('empréstimo aprovado!')



