setASize = int(input())

setA = set(map(int, input().split()))

tasks = int(input())

for i in range(tasks):
    splits = str(input()).split(' ')
    cmd = splits[0]
    
    if (cmd == "update"):
        nums = splits[1]
        setUpdate = set(map(int, input().split()))
        
        setA.update(setUpdate)
        
    elif (cmd == "intersection_update"):
        nums = splits[1]
        setUpdate = set(map(int, input().split()))
        setA.intersection_update(setUpdate)
        
    elif (cmd == "symmetric_difference_update"):
        nums = splits[1]
        setUpdate = set(map(int, input().split()))
        setA.symmetric_difference_update(setUpdate)
        
    elif (cmd == "difference_update"):
        nums = splits[1]
        setUpdate = set(map(int, input().split()))
        setA.difference_update(setUpdate)
        
print(sum(setA))