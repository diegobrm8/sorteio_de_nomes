import random
from time import sleep

lados_do_dado = 6
numero_de_dados = 1

# Simula o lançamento dos dado
resultados = [random.randint(1, lados_do_dado) for _ in range(numero_de_dados)]
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print('''ATENÇÃO!!''')
sleep(1)
# Imprime os resultados
print(f"O resultado foi: {resultados}")
