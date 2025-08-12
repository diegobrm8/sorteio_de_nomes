import random

def main():
    print("=== SORTEADOR DE NOMES ===")
    nomes = []

    while True:
        nome = input("Digite um nome (ou 'fim' para encerrar): ")
        if nome.lower() == "fim":
            break
        nomes.append(nome)

    if not nomes:
        print("Nenhum nome foi adicionado!")
        return

    sorteado = random.choice(nomes)
    print(f"\n🎯 O nome sorteado foi: {sorteado}")

    salvar = input("Quer salvar o resultado? (s/n) ")
    if salvar.lower() == "s":
        with open("resultado.txt", "w", encoding="utf-8") as f:
            f.write(f"Nome sorteado: {sorteado}\n")
        print("✅ Resultado salvo em 'resultado.txt'.")

if __name__ == "__main__":
    main()
