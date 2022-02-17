# a = input().split()
# str1 = '-'.join(a)
# print(str1)


def split_and_join(line):
    x=line.split(" ") 
    x='-'.join(x)    
    return x

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result