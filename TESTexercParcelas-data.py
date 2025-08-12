from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 5_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=2)
data_final = data_emprestimo + delta_anos


data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas

print(numero_parcelas, 'parcelas')
for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)

print('-=' *30)
import datetime

data_hora_atual = datetime.datetime.now()
data_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
print(data_formatada)

data_string = "23/07/2023 10:30:15"
data_objeto = datetime.datetime.strptime(data_string, "%d/%m/%Y %H:%M:%S")
print(data_objeto)  # Saída: 2023-07-23 10:30:15
