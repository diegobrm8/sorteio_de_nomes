import os
import shutil

diretorio = '.py'

if os.path.exists(diretorio) and os.path.isfile(diretorio):
    try:
        os.remove(diretorio)
        print(f'O diretório {diretorio} foi excluído com sucesso.')
    except Exception as e:
        print(f"Erro ao excluir o diretório {diretorio}: {str(e)}")
else:
    print(f'O diretório {diretorio} não existe ou não é um diretório válido.')



diretorio = 'CRIARPASTA.py'

if os.path.exists(diretorio) and os.path.isdir(diretorio):
    try:
        shutil.rmtree(diretorio)
        print(f'O diretório {diretorio} foi excluído com sucesso.')
    except Exception as e:
        print(f"Erro ao excluir o diretório {diretorio}: {str(e)}")
else:
    print(f'O diretório {diretorio} não existe ou não é um diretório válido.')
