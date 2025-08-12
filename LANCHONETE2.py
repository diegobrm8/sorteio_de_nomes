def exibir_menu():
    print("=== Menu da Lanchonete ===")
    print("1. cachorro quente - R$10.00")
    print("2. batata frita - R$7.50")
    print("3. refrigerante - R$8.00")
    print("4. Hamburger - R$10.00")
    print("5. Xis - R$13.50")
    print("6. cerveja - R$4.50")
    print('7. Sair')


def selecionar_item():
    opcao = input("Selecione um item do menu (1-7): ")
    return opcao


def processar_pedido(opcao, total):
    if opcao == "1":
        total += 10
        print("Você escolheu um cachorro quente.")

    elif opcao == "2":
        total += 7.50
        print("Você escolheu batata frita.")

    elif opcao == "3":
        total += 8.00
        print("Você escolheu refrigerante.")

    elif opcao == "4":
        total += 10.00
        print("Você escolheu Hamburger!")

    elif opcao == "5":
        total += 13.50
        print("Você escolheu Xis")

    elif opcao == "6":
        total += 4.50
        print('Você escolheu cerveja')

    elif opcao == '7':
        print("saindo... Muito obrigado pelo pedido...!")

    else:
        print("Escolha inválida. Por favor, tente novamente.")
    return total


def calcular_total(pedido):
    total = sum(pedido.values())
    return total


def main():
    pedido = {}
    while True:
        exibir_menu()
        opcao = selecionar_item()
        if opcao == '7':
            break
        pedido[opcao] = processar_pedido(opcao, pedido.get(opcao, 0))
    total = calcular_total(pedido)
    print(f"Total do pedido: R${total:.2f}")


if __name__ == '__main__':
    main()
