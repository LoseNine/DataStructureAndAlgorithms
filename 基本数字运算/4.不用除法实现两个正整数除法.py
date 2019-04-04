def Divide(n,m):
    res=0
    while n>=m:
        n-=m
        res+=1
    print("商为%d 余数为%d"%(res,n))

if __name__ == '__main__':
    Divide(6,3)