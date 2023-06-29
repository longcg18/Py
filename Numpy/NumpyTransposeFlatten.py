import numpy

n, m = map(int, input().split())

lst = numpy.array([input().split() for _ in range(n)], int)
print(lst.transpose(), lst.flatten(), sep='\n')