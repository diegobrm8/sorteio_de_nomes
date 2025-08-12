produto = (float(input('digite o valor:')))
dav = (produto*0.1)
davc = (produto*0.05)
print('pagamento à vista = 1')
print('pagamento à vista cartão = 2')
print('pagamento 2x cartão = 3')
print('pagamento 3x ou mais cartão = 4')
opção = int(input('digite sua opção de pagamento:'))

if opção == 1:
    print(f'O valor é de:{(produto-dav)}')
elif opção == 2:
    print(f'O valor é de:{(produto-davc)}')
elif opção == 3:
    print(f'0 valor é de:{produto}')
elif opção == 4:
    print(f'O valor é de:{produto+(produto*0.2)}')



