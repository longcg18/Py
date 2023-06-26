def print_formatted(number):
    # your code goes here
    bin_max = str(bin(int(number))[2:])
    bin_len = len(bin_max)
    for i in range(1, number+1):
        print(str(i).rjust(bin_len, ' '), 
              str(oct(int(i)))[2:].rjust(bin_len, ' '), 
              str(hex(int(i)))[2:].upper().rjust(bin_len, ' '),
              str(bin(int(i)))[2:].rjust(bin_len, ' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)