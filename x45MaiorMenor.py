listanum = []
maior = 0
menor = 0
for c in range (0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c+1}:')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print(f'Você digitou os valores {listanum}')
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')



