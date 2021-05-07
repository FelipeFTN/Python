import numpy

table = numpy.array([['A', 'B', 'C'],
                     ['D', 'E', 'F'],
                     ['G', 'H', 'I']])

for x in range(3): #VERIFICA A PRIMEIRA COLUNA
    print(table[x, 0])

for x in range(3): #VERIFICA A SEGUNDA COLUNA
    print(table[x, 1])

for x in range(3): #VERIFICA A TERCEIRA COLUNA
    print(table[x, 2])

for x in range(3): #VERIFICA A PRIMEIRA LINHA
    print(table[0, x])

for x in range(3): #VERIFICA A SEGUNDA LINHA
    print(table[1, x])

for x in range(3): #VERIFICA A TERCEIRA LINHA
    print(table[2, x])

for x in range(3): #VERIFICA DIAGONAL ESQUEDA
    print(table[x, x])
    x = x + 1

for x in range(3): #VERIFICA DIAGONAL DIREITA
    print(table[x, x])
    x = x - 1