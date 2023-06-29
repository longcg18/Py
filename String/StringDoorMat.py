"""
N = 7 & M = 3N

Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
"""

N, M = int(input().split(" "))
welcome= "WELCOME"
symbole= ".|."
for i in range(0,int((N-1)/2)+1):
    if i == int((N-1)/2):
        print(welcome.center(M,"-"))
        break

    if i < int((N-1)/2):
        temp=symbole*(2*i+1)
        print(temp.center(M,"-"))
        
for i in range(int((N-1)/2)-1,-1,-1):
    temp=symbole*(2*i+1)
    print(temp.center(M,"-"))