nome =str(input('Qual é o seu nome?'))
if nome == 'Diego':
    print('Que nome bonito!')
elif nome == 'Douglas' or nome == 'Luana' or nome == 'Bruno':
    print('Que nome estranho!')
else:
    print('seu nome é bem comum!')
print(f'Bom dia!{nome}.')
