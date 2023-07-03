# Enter your code here. Read input from STDIN. Print output to STDOUT

K, M = input().split()
K = int(K)
M = int(M)
SUM = 0

for k in range (K):
    #n = int(input())
    
    N = map(int, input().split())
    N = list(N)
    n = []
    for i in range (1, int(N[0])+1):
        n.append(N[i])
    max_Ni = max(n)
    #print(max_Ni)
    SUM += max_Ni**2
    print(SUM)

print(SUM % M)
    