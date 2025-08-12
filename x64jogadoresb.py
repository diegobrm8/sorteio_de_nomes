jogador = dict()
partidas = list()
jogador["nome"] = str(input('nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
jogador["partidas"] = tot
jogador["gols"] = partidas[:]
jogador["total"] = sum(partidas)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-=' * 30)
print(f'{jogador["nome"]} jogou {len(jogador["gols"])} partidas ')
for k, v in enumerate(jogador["gols"]):
    print(f'na partida {k+1} foram {v} gols')
print(f'foi um total de {jogador["total"]} gols')
