K = int(input())

cus = list(input().split())
fam = set()
cap = set()

for i in cus:

    if i not in cap and i not in fam:
        cap.add(i)
    else:
        cap.discard(i)
        fam.add(i)
print(*cap)
    