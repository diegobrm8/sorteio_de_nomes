import os


caminho_procura = 'C:\Users\diego\OneDrive\Área de Trabalho\pastas\cursoUdemyVscode'

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        caminho_completo = os.path.join(raiz, arquivo)
        print(caminho_completo)
