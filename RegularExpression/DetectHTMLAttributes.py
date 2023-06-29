import re
N = int(input())
output = {}
for i in range(0,N):
    match = re.findall(r'<[^/].*?>', input())
    for m in match:
        tag = re.match(r'<([^ >]*)', m)[1]
        attributes = re.findall(r'\s([^ =]*)=', m)
        if tag in output:
            output[tag] += attributes
        else:
            output[tag] = attributes
for tag in output:
    output[tag] = sorted(list(set(output[tag])))
for key in sorted(list(output.keys())):
    print(f'{key}:{",".join(output[key])}')