from collections import Counter


if __name__ == '__main__':
    s = input()
    counter = Counter( list(sorted(s)))
    
    print('\n'.join(k+ ' ' + str(v) for k, v in counter.most_common(n=3)) )