def JudegTwo(number):
    if number<=0:
        return False
    i=1
    while i<=number:
        if i==number:
            return True
        i=i<<1          #每次二进制左移一位
    return False

def JudegTwo2(number):
    if number<=0:
        return False
    n=number&(number-1)
    return n==0

if __name__ == '__main__':
    print(JudegTwo(2))
    print(JudegTwo(3))

    print(JudegTwo2(2))
    print(JudegTwo2(3))
