from datetime import datetime

ano_nasci = int(input('Em que ano você nasceu? '))
mes_nasci = int(input('Em que mês você nasceu? '))
dia_nasci = int(input('Em que dia você nasceu? '))

data_nasci = datetime(ano_nasci, mes_nasci, dia_nasci)
data_atual = datetime.now()

diff = data_atual - data_nasci
dias = diff.days
anos, dias = dias // 365, dias % 365
meses, dias = dias // 30, dias % 30
print(f'Você tem {anos} anos, {meses} meses e {dias} dias!')
