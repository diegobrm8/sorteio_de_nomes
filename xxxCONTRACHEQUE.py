def calcular_salariobruto(horas_trabalhadas, valor_horas):
    salario_bruto = horas_trabalhadas * valor_horas
    return salario_bruto


def calcular_inss(salario_bruto):
    if salario_bruto <= 1100:
        inss = salario_bruto * 0.075
    elif salario_bruto <= 2203.48:
        inss = salario_bruto * 0.09
    elif salario_bruto <= 3305.22:
        inss = salario_bruto * 0.12
    elif salario_bruto <= 6433.57:
        inss = salario_bruto * 0.14
    else:
        inss = 751.99
    return inss


def calcular_salario_liquido(salario_bruto, inss, irrf):
    """Calcula o salário líquido dado o salário bruto, a contribuição do INSS e do IRRF."""
    salario_liquido = salario_bruto - inss - irrf
    return salario_liquido


def calcular_irrf(salario_bruto, inss):
    """Calcula a contribuição do IRRF dado o salário bruto e a contribuição do INSS."""
    salario_base = salario_bruto - inss
    if salario_base <= 1903.98:
        irrf = 0
    elif salario_base <= 2826.65:
        irrf = salario_base * 0.075 - 142.80
    elif salario_base <= 3751.05:
        irrf = salario_base * 0.15 - 354.80
    elif salario_base <= 4664.68:
        irrf = salario_base * 0.225 - 636.13
    else:
        irrf = salario_base * 0.275 - 869.36
    return irrf


horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
valor_horas = float(input("Digite o valor das horas trabalhadas: "))

salario_bruto = calcular_salariobruto(horas_trabalhadas, valor_horas)
inss = calcular_inss(salario_bruto)
irrf = calcular_irrf(salario_bruto, inss)
salario_liquido = calcular_salario_liquido(salario_bruto, inss, irrf)

print("Salário bruto: R$", salario_bruto)
print("Contribuição do INSS: R$", inss)
print("Contribuição do IRRF: R$", irrf)
print("Salário líquido: R$", salario_liquido)
