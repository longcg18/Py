def validate(string):
    str_len = len(string)
    if (str_len != 10):
        return 'NO'
    if ((string)[0] != '7') & (string[0] != '8') & (string[0] != '9'):
        return 'NO'    
    for i in string:
        if (i.isdigit()) == False: 
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    N = int(input())
    inputs = []
    for i in range (0, N):
        string = str(input())
        inputs.append(string)
    for i in range (0, N):
        print(validate(inputs[i]))
    