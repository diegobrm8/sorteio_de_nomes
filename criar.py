from pathlib import Path

caminho_do_arquivo_py = Path('Json.py')

#  caminho_do_arquivo_py.write_text("# Seu código Python aqui\nprint('Olá, mundo!')\n")
caminho_do_arquivo_py.touch()
print(f"Arquivo '{caminho_do_arquivo_py}' criado com sucesso.")

# caminho_do_arquivo_py.unlink()
