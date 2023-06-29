import numpy

rows, cols = map(int, input().split())
attrs = ['add', 'subtract', 'multiply',
         'floor_divide', 'mod', 'power']

a = numpy.array([input().split() for row in range(rows)], int)
b = numpy.array([input().split() for row in range(rows)], int)

for attr in attrs:
    print(getattr(numpy, attr)(a, b))