import datetime


def esta_na_hora(hora, minuto, data_atual):
    if data_atual.hour == hora and data_atual.minute == minuto:
        return True
    return False


print('''DESPERTADOR!''')
hora_string = input('Que horas você quer acordar? (hh:mn): ')
dia_da_semana = input('Que dias da semana? (seg ter qua qui sex sab dom):')
hora = int(hora_string.split(':')[0])
minuto = int(hora_string.split(':')[1])
agora = datetime.datetime.now()
resultado = esta_na_hora(hora, minuto, agora)
print('Esta na hora? :' + str(resultado))
