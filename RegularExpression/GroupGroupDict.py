import re

s = input()

def result(s):
    ss = re.search('[a-zA-Z0-9]+',s)[0]
    result=-1
    for i in range(len(ss)-1):
        if ss[i]==ss[i+1]:
            return ss[i]
    return result

print(result(s))