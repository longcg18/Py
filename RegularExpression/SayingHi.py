re_pattern = r'^[Hh][Ii]\s[^Dd]'

import re

N = int(input())

str_list = []
for i in range (N):
    str_list.append(str(input()))
    
for i in range (N):
    if (bool(re.search(re_pattern, str(str_list[i])))): 
        print(str_list[i])
        