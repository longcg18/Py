import re
from sys import stdin

java = r'public class|java\.io'
c = r'#include'

code = ''.join(stdin.read())

if re.search(java, code):
    print('Java')
elif re.search(c, code):
    print('C')
else:
    print('Python')