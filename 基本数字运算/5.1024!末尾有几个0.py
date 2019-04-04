def zeroCount(n):
    count=0
    while n>0:
        n=n//5
        count+=n
    return count

if __name__ == '__main__':
    print(zeroCount(1024))