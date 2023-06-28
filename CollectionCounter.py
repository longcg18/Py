from collections import Counter

n_shoes = int(input())

shoes_availables = input().split()
size_number = Counter(shoes_availables)

n_customers = int(input())

money = 0

for i in range(n_customers):
    size, price = input().split()
    
    if size_number[size] > 0:
        size_number[size] -= 1
        
        money += int(price)
        
print(money)