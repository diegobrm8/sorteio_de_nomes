def ficha(jog='desconhecido', gol=0):
    print(f'o jogador {jog} fez {gol} gols no campeonato')


while True:
    n = str(input('Nome do jogador: '))
    g = str(input('Quantos gols ele fez? '))
    if n.isnumeric():
        print('\033[0;31mERRO! Digite um nome.\033[m')
    else:
        break

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
