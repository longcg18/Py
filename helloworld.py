
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
"""

n=int(input())

for i in range(1, n):
    print(i * (10 ** i // 9))