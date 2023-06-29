import re

lines=[]
for _ in range(int(input())):
    lines.append(input())

for _ in range(int(input())):
    test = input()
    pattern = test[:-2]+'[zs]'+test[-1]
    qtt = 0
    for line in lines:
        qtt = qtt + len(re.findall(pattern, line))
    print(qtt)