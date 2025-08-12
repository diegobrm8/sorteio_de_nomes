turma = [['gustavo', 40], ['leo', 23], ["Jackson", 30], ["Camila", 30], ["Lea", 27]]
galera = [turma[:]]
for indice, pessoa in enumerate(turma):
    print(f' {indice+1} {pessoa[0]}, tem {pessoa[1]} anos')

print('-=' * 30)

print()
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')
