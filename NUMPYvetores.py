# vetores são utilizados em análises matemáticas e algebras pois podemos fazer manipulações e rep. e modelagem do mundo r.

import numpy

a = numpy.array([1, 2, 3, 4, 5])  # tds elementos devem ser do mesmo tipo
vetor = numpy.array(a)
print(vetor)
print(type(vetor[2]))
lista = [1, 2, 3, 4, 5, '6']
vetor2 = numpy.array(lista)  # transf tudo em string(str)
print(vetor2)
vetor3 = numpy.array([1, 2, 3, 4, 5, 6, 'a'])
print(vetor3)
