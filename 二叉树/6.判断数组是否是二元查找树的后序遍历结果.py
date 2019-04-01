def isAfterOrder(arr,start,end):
    if arr==None:
        return
    #先找出根节点，然后分而治之
    root=arr[end]

    i=start
    while i<end:
        if(arr[i]>root):
            break
        i+=1
    j=i
    while j<end:
        if arr[j]<root:
            return False
        j+=1
    left_isAfterOrder=True
    right_isAfterOrder=True
    if i>start:
        left_isAfterOrder=isAfterOrder(arr,start,i-1)
    if j<end:
        right_isAfterOrder=isAfterOrder(arr,i,end)
    return left_isAfterOrder and right_isAfterOrder

if __name__ == '__main__':
    arr=[1,3,2,5,6,7,4]
    result=isAfterOrder(arr,0,len(arr)-1)
    i=0
    while i<len(arr):
        print(arr[i])
        i+=1
    if result:
        print("Yes")
    else:
        print(
            "No"
        )