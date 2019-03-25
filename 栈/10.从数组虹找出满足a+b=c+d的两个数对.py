class pair:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.sum=x+y
res=dict()
def findpari(arr):
    al=len(arr)
    for i in range(al-1):
        for j in range(i+1,al):
            p=pair(arr[i],arr[j])
            res[p]=p.sum

if __name__ == '__main__':
    arr=[3,4,7,10,20,9,8]
    findpari(arr)
    for v in res:
        for k in res:
            if v!=k and v.sum==k.sum and v.x!=k.x and v.y!=k.y:
                print(v.x,v.y)
                print(k.x,k.y)