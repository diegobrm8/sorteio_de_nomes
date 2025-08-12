# casa é num dividido por 17


número = 0

while número <= 100:
    número += 1
    if número % 10 == 0 or número % 10 == 6:
        continue
    if número % 17 == 0:
        print(número)

# usando break fica

# numero = 0
# while True:
# numero += 1
# if numero < 1000:
# break
