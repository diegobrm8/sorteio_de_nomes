
usuário = str(input('Nome do usuário: '))
senha = input('Digite sua senha: ')


usuáriobd = 'diegobrm8'
senha_bd = 'Faithnomore8'

if usuáriobd == usuário and senha_bd == senha:
    print('\033[32mVocê está logado no sistema!\033[m')

else:
    print('\033[31mUsuário ou senha inválidos!\033[m')
