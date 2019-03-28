class Node:
    def __init__(self,x=None):
        self.x=x
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

def printTree(root):
    queue=[root]
    while len(queue)!=0:
        root=queue.pop(0)
        print(root.data)
        if root.left!=None:
            queue.append(root.left)
        if root.right!=None:
            queue.append(root.right)
if __name__ == '__main__':
    arr=[i for i in range(1,5)]
    root=arraytotree(arr,0,len(arr)-1)
    cur=root
    printTree(root)