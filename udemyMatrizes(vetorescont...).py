import numpy

m = numpy.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
print(m)
print('-=' * 35)
print(m[1, 1])
print(m[:, 2])  # : ->toda a coluna 3,5,8
print(m[1, :])  #: -> toda a linha 3,4,5
