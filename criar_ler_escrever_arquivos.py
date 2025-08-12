# http://docs.python.org/3/library/functions.html#open
file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)
print('Lendo linhas:')
print(file.read())
print('-' * 30)

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('-' * 30)
file.seek(0)
for linha in file.readlines():
    print(linha, end='')
file.close()
