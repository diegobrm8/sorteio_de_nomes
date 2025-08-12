def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade >= 18:
        return f' com idade {idade} anos pode votar'
    else:
        return f' com {idade} anos não pode votar ainda, espere completar 18 anos.'


nasci = int(input('Em que ano você nasceu? '))
print(voto(2000))
print(voto(2010))
print(voto(1969))
print(voto(nasci))
