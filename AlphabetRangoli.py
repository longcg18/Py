ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'

def print_rangoli(size):
    string = ALPHABETS[:size]
    
    pattern = []
    length = size * 4 - 3
    
    for letter in string[::-1]:
        pattern.append(letter)
        print('-'.join(pattern + pattern[-2::-1]).center(length, '-'))
    
    for element in range(len(pattern) - 1):
        pattern.pop()
        print('-'.join(pattern + pattern[-2::-1]).center(length, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)