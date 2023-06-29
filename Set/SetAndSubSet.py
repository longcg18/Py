tasks = int(input())
results = []

for i in range (tasks):
    setASize = int(input())
    setA = set(map(int, input().split()))
    
    setBSize = int(input())
    setB = set(map(int, input().split()))
    
    if (setA.issubset(setB)):
        results.append("True")
    else:
        results.append("False")

for i in results:
    print(i)