class Node:
    def __init__(self,x=None):
        self.data=x
        self.left=None
        self.right=None

def arraytotree(arr,start,end):
    root=None
    if end>=start:
        root=Node()
        mid=(start+end+1)//2
        root.data=arr[mid]
        root.left=arraytotree(arr,start,mid-1)
        root.right=arraytotree(arr,mid+1,end)
    else:root=None
    return root
#中序遍历打印
def printTree(root):
    if root==None:
        return
    if root.left!=None:
        printTree(root.left)
    print(root.data)
    if root.right!=None:
        printTree(root.right)

if __name__ == '__main__':
    arr=[i for i in range(1,5)]
    root=arraytotree(arr,0,len(arr)-1)
    printTree(root)