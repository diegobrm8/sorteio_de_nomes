usuarios = {}


def registrar_usuario():
    print("Registro de Usuário")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    usuarios[nome] = senha
    print("Usuário registrado com sucesso!\n")


def fazer_login():
    print("Login")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

    if nome in usuarios and usuarios[nome] == senha:
        print("Login bem-sucedido! Bem-vindo,", nome)
    else:
        print("Login falhou. Verifique seu nome de usuário e senha.\n")


# Loop principal
while True:
    print("1. Registrar")
    print("2. Fazer Login")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        registrar_usuario()
    elif escolha == "2":
        fazer_login()
    elif escolha == "3":
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
