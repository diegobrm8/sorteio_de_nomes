jogo = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('   a  b  c')
conta = 0
#jogo[1][0] = 4
#jogo[1][1] = 4
#jogo[1][2] = 4

for linha in jogo:
    print(conta, linha)


print()
print('=-' * 30)
print()
print('   a  b  c')
for conta, linha in enumerate(jogo):
    conta += 1
    print(conta, linha)
