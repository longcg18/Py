n = int(input())
s = set(map(int, input().split()))
Tasks = int(input())
for i in range (Tasks):
    splits = input().split(' ')
    cmd = str(splits[0])
    
    if (cmd == "pop"):
        s.pop()
    if (cmd == "remove"):
        val = int(splits[1])
        s.remove(val)
    if (cmd == "discard"):
        val = int(splits[1])
        s.discard(val)
    if (cmd == "print"):
        print(s)

print(sum(s))