from itertools import combinations

S, K = input().split()
S = ''.join(sorted(S))
K = int(K)

for k in range(K):
    com = combinations(S, k+1)
    for c in com:
        c = ''.join(c)
        print(c)