def JudgePow(number):
    if number<0:
        return False
    i=1
    while i<number:
        m=i*i
        if m==number:
            return True
        elif m>number:
            return False
        i+=1
    return False

if __name__ == '__main__':
    n=15
    n2=16
    print(JudgePow(n))
    print(JudgePow(n2))