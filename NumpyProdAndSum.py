import numpy

rows, cols = map(int, input().split())

a = numpy.array([input().split() for row in range(rows)], int)
#b = numpy.array([input().split() for row in range(rows)], int)

c = numpy.sum(a, axis = 0)

d = numpy.prod(c)

print(d)