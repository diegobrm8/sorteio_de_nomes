import shutil
import os

# Defina o caminho da pasta de origem e de destino
pasta_origem = r'C:\Users\diego\ExerciciosECursosPython'
pasta_destino = r'C:\Users\diego\EXERCICIOSPYTHON'

# Verifique se a pasta de destino existe e, se não, crie-a
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Obtenha uma lista de todos os arquivos na pasta de origem
arquivos = os.listdir(pasta_origem)

# Copie cada arquivo da pasta de origem para a pasta de destino
for arquivo in arquivos:
    caminho_origem = os.path.join(pasta_origem, arquivo)
    caminho_destino = os.path.join(pasta_destino, arquivo)
    shutil.copy2(caminho_origem, caminho_destino)

print("Todos os arquivos foram copiados com sucesso!")
