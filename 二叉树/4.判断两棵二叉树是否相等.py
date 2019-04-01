class Node:
    def __init__(self,x=None):
        self.data=x
        self.left=None
        self.right=None
def ifEqual(root1,root2):
    if root1==None and root2==None:
        return True
    if root1==None and root2!=None:
        return False
    if root1!=None and root2==None:
        return False
    if root1.data==root2.data:
        return ifEqual(root1.left,root2.left) and ifEqual(root1.right,root2.right)
    else:
        return False
def arrays(arr,start,end):
    root=None
    if end>=start:
        root=Node()
        mid=(start+end+1)//2
        root.date=arr[mid]
        left=arrays(arr,start,mid-1)
        right=arrays(arr,mid+1,end)
    else:
        return None
    return root
if __name__ == '__main__':
    arr=[1,2,3,4]
    a1=arrays(arr,0,len(arr)-1)
    a2= arrays(arr, 0, len(arr) - 1)
    print(ifEqual(a1,a2))