from itertools import groupby

S = str(input())

x = [(len(list(v)),int(k)) for k,v in groupby(S)]
print(*x)