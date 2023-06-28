setA_size = int(input())
setA = set(map(int, input().split()))

setB_size = int(input())

setB = set(map(int, input().split()))

print(len(setA.symmetric_difference(setB)))