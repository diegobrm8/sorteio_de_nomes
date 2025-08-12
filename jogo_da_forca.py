import random


def escolher_palavra():
    palavras = ["python", "programacao", "computador", "algoritmo", "desenvolvimento"]
    return random.choice(palavras)


def jogar_forca():
    palavra = escolher_palavra()
    letras_certas = []
    tentativas = 5


    print("\033[32mBem-vindo ao Jogo da Forca!\033[0m")
    while tentativas > 0:
        palavra_secreta = ''
        for letra in palavra:
            if letra in letras_certas:
                palavra_secreta += letra
            else:
                palavra_secreta += "_"
        print("\nPalavra secreta:", palavra_secreta)
        print(f"Tentativas restantes: {tentativas}")

        if palavra_secreta == palavra:
            print("Parabéns! Você venceu!")
            break

        if tentativas == 0:
            print(f"\031Fim de jogo! A palavra era '{palavra}'.\033[om")
            break

        if palavra_secreta == palavra:
            print("\033Parabéns! Você venceu!\033[0m")
            break

        letra_escolhida = input("Escolha uma letra: ").lower()

        if letra_escolhida in palavra:
            letras_certas.append(letra_escolhida)
        else:
            tentativas -= 1
            print("Letra errada. Tente novamente!")

    if tentativas == 0:
        print(f"Fim de jogo! A palavra era '{palavra}'.")


jogar_forca()
