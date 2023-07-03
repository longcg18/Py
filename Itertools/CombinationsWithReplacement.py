from itertools import combinations_with_replacement

S, K = input().split()

S = ''.join(sorted(S))

K = int(K)

com = combinations_with_replacement(S, K)

for c in com:
    print(''.join(c))