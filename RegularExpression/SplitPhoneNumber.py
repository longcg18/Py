re_pattern = r"^([0-9]{1,3})[- ]([0-9]{1,3})[- ]([0-9]{4,10})$"

import re

N = int(input())

str_list = []
for i in range (N):
    str_list.append(str(input()))
    
for i in range (N):
    string_line = re.findall(re_pattern, str_list[i])
    print("CountryCode=" + string_line[0][0] + ",LocalAreaCode=" + string_line[0][1] + ",Number=" + string_line[0][2])
