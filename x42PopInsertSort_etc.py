num = [2, 7, 6, 9, 2, 3, 5, 11, 4]
num[3] = 8
num.append(342)
print(num)
print('-' * 30)
num = [2, 4, 6, 9, 2, 3, 8, 11]
num.sort()
num.insert(2, 18)
print(num)
print('-' * 30)
# num.sort(reverse=True) vaileraocontrário
# num.pop() removeoselecionado
# num.remove() RemoveoselecionadoSE,TEM,2,REMOVE,O,PRIMEIRO

num = [2, 4, 6, 9, 2, 3, 8, 11, 7]
print(num.sort(reverse=True))
print(num)
print('-' * 30)

num = [1, 2, 3, 4, 5]
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')
