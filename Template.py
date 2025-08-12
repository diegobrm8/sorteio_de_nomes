import string

template = string.Template('''
De: $remetente
Para: $destinatario
Assunto: $assunto

$corpo
Atenciosamente,
$remetente
''')

informacoes = {
    'remetente': 'Diego',
    'destinatario': 'Maya',
    'assunto': 'Reunião de amanhã',
    'corpo': 'Olá Jane, a reunião de amanhã foi adiada para as 14:00. Por favor, '
    'confirme sua presença.'
}

email = template.substitute(informacoes)
print(email)