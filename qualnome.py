while True:
    nome = str(input('qual é o seu nome? ')).strip().capitalize()
    if nome == 'Diego':
        print("ola Diego, bom dia")
        break
    else:
        print('\033[31mnome invalido, digite seu nome\033[0m')
