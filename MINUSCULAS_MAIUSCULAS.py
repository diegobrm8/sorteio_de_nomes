def fazAlgo(string):
    pos = len(string) - 1
    stringMi = string.lower()
    string = string.upper()
    stringRe = ""
    while pos >= 0:
        if string[pos] == 'A' or string[pos] == 'E' or string[pos] == 'I' or string[pos] == 'O' or string[pos] == 'U':
            stringRe = stringRe + string[pos]
        else:
            stringRe = stringRe + stringMi[pos]
        pos = pos - 1
    return stringRe


def maiusculas(string):
    return string.upper()


print(maiusculas('Programamos em python 2?'))

print(maiusculas('Programamos em Python 3.'))

print(maiusculas('PrOgRaMaMoS em python!'))
