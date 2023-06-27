from collections import deque
T = int(input())
for _ in range(T):
    n = int(input())
    sideLengths = list(map(int, input().split()))
    d = deque(sideLengths)
    sup = max(d[0], d[-1])
    sup_temp = sup
    while len(d) != 0 and sup == sup_temp:
        if d[0] > d[-1]:
            sup = d.popleft()
        else:
            sup = d.pop()
        if sup <= sup_temp:
            sup_temp = sup
    if len(d) == 0:
        print('Yes')
    else:
        print('No')