import numpy as np

N,M,P = map(int,input().split())

A1 = np.array([input().split() for _ in range(N)],int)

A2 = np.array([input().split() for _ in range(M)],int)

print(np.concatenate((A1,A2)))