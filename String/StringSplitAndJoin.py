def split_and_join(line):
    # write your code here
    splited_string = line.split(' ')
    joined_string = '-'.join(splited_string)
    return joined_string
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)