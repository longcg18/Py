def count_substring(string, sub_string):
    str_len = len(string)
    sub_len = len(sub_string)
    count = 0
    if (str_len < sub_len): 
        return 0
    i = 0
    while(i < str_len):
        if (string[i] == sub_string[0]):
            pString = string[i:sub_len+i]
            if (sub_string == pString):
                count = count + 1
        i = i + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)