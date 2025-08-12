import string

template = string.Template('$nivel : $mensagem')

log_info = {'nivel': 'INFO', 'mensagem': 'Operação bem sucecida.'}


log_mensagem = template.substitute(log_info)
print(log_mensagem)
