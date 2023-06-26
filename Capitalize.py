def solve(s):
    s = s.lower()
    sList = s.split(' ')
    for i in sList:
        #print(i)
        i = i.capitalize()
        print(i, end=' ')
    #s = ' '.join(sList)
    #print(s)

if __name__ == '__main__':
    input_string = str(input())

    solve(input_string)