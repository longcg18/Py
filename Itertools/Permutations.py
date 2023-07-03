from itertools import permutations

S, K = input().split()
K = int(K)

S = ''.join(sorted(S))

arr = list(permutations(S, K))

for i in range (len(arr)):
    print(''.join(arr[i]))
#print(*permutations(S, K))