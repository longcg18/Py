import numpy

numpy.set_printoptions(legacy='1.13')

my_arr = numpy.array(list(map(float, input().split())))

print(numpy.floor(my_arr))

print(numpy.ceil(my_arr))

print(numpy.rint(my_arr))