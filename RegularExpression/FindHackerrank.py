start = r'^hackerrank'
end = r'hackerrank$'
only = r'^hackerrank$'

import re

N = int(input())

str_list = []
for i in range (N):
    str_list.append(str(input()))
    
for i in range (N):
    if (bool(re.search(only, str(str_list[i])))): 
        print("0")
    elif (bool(re.search(start, str(str_list[i])))):
        print("1")
    elif (bool(re.search(end, str(str_list[i])))):
        print("2")
    else:
        print("-1")
        