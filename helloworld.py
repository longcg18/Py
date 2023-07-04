
"""
n=int(input())

if (((n % 2) != 0) | ((n % 2 == 0) & (n >= 6) & (n <= 20))):
    print("Weird")
else: 
    print("Not Weird")
"""

"""
a = int(input())
b = int(input())

print(a//b)
print(a/b)
"""

"""
n=int(input())

for i in range(n):
    print(i*i)
"""
"""
def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                leap=True
            else: 
                leap=False
        else: 
            leap=True
    
    
    return leap

year = int(input())
print(is_leap(year))
"""


"""
if __name__ == '__main__':
    n = int(input())
var=""

for i in range(n):
    j=str(i+1)
    var+=j    
print(var)
"""

"""
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a+b, a-b, a*b, sep="\n")
"""


"""
s=str(input())

temp2="" #alpha
temp3="" #upper
tempOdd="" #odd
tempEven="" #even
for i in range(len(s)):
    if (s[i].isnumeric()):
        if((int(s[i]) % 2) == 0):
            tempEven+=str(s[i])
        if((int(s[i]) % 2) != 0):
            tempOdd+=str(s[i])
    else:
        if(s[i].isupper()):
            temp3+=s[i]
        else:
            temp2+=s[i]

b=sorted(temp2) #alpha
c=sorted(temp3) #upper
odd=sorted(tempOdd) # odd
even=sorted(tempEven) # even
f=""
for i in range(len(b)):
    f+=b[i]    

for i in range(len(c)):
    f+=c[i]

for i in range(len(odd)):
    f+=odd[i]

for i in range(len(even)):
    f+=even[i]

print(f)

#print(sorted(temp2)+sorted(temp3)+sorted(temp1))

#print(temp1, temp2, temp3)

"""


"""
n=int(input())

for i in range(1, n):
    print(i * (10 ** i // 9))

"""
# Problem: What's your name?
def print_full_name(first, last):
    # Write your code here
    # Hello firstname lastname! You just delved into python.
    print("Hello ", first, " ", last, "! You just delved into python.", sep="")



if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# Problem: Mutable String

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    
    
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


### List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    
    print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i, j, k]) != n])