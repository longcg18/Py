_, numbers = input(), input().split()
checks = [(int(i) > 0, i == i[::-1]) for i in numbers]
print(all([i[0] for i in checks]) and any(i[1] for i in checks))