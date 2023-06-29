Regex_Pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'

import re

N = int(input())

pan_list = []
for i in range (N):
    pan_list.append(str(input()))
    
for i in range (N):
    if (bool(re.search(Regex_Pattern, str(pan_list[i])))): 
        print("YES")
    else:
        print("NO")
        