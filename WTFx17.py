número = input('digite um número:')
espaços = '0000'
junção = espaços + número
tamanho = len(junção)
print('unidade:', junção[tamanho - 1])
print('dezena:', junção[tamanho - 2])
print('centena', junção[tamanho - 3])
print('milhar', junção[tamanho - 4])
