import numpy

rows, cols = map(int, input().split())

a = numpy.array([input().split() for row in range(rows)], int)

b = numpy.min(a, axis=1)

c = numpy.max(b)

print(c)