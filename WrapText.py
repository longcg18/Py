import textwrap

"""
ABCDEFGHIJKLMNOPQRSTUVXWYZ                                  
4
>
ABCD
EFGH
IJKL
MNOP
QRST
UVXW
YZ
"""

def wrap(string, max_width):
    return '\n'.join(textwrap.TextWrapper(max_width).wrap(text=string))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)