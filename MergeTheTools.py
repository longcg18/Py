import textwrap

def merge_the_tools(string, k):
    t = []
    t = textwrap.TextWrapper(k).wrap(string)
    u = []
    for i in t:
        temp = set(i)
        u.append(''.join(temp))
    for i in u:
        print(i) 
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)