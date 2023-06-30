n, x = map(int, input().split())

def avg(a):
    return sum(a) / len(a)

result = [avg(i) for i in zip(*[list(map(float, input().split()[:n])) for _ in range(x)])]
print(*result, sep='\n')