class Node:
    def __init__(self,x=None):
        self.data=x
        self.right=None
        self.left=None
class Stack:
    def __init__(self):
        self.arr=[]
    def is_empty(self):
        return len(self.arr)==0
    def push(self,x):
        self.arr.append(x)
    def pop(self):
        if self.is_empty():
            return None
        return self.arr.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.arr[-1]
def getPathFromRoot(root,node,s):
    if root==None:
        return False
    if root==node:
        s.push(root)
        return True
    if getPathFromRoot(root.left,node,s) or getPathFromRoot(root.right,node,s):
        s.push(root)
        return True
    return False
def FindParentNode(root,node1,node2):
    stack1=Stack()
    stack2=Stack()
    getPathFromRoot(root,node1,stack1)
    getPathFromRoot(root, node2, stack2)
    commentParent=None
    while stack1.peek()==stack2.peek():
        commentParent=stack1.peek()
        stack1.pop()
        stack2.pop()
    return commentParent

def arrTotree(arr,start,end):
    root=None
    if start<=end:
        root=Node()
        mid=(start+end+1)//2
        root.data=arr[mid]
        root.left=arrTotree(arr,start,mid-1)
        root.right=arrTotree(arr,mid+1,end)
    else:
        return
    return root

if __name__ == '__main__':
    arr=[i for i in range(1,10)]
    root=arrTotree(arr,0,len(arr)-1)
    node1=root.left.left.left
    node2=root.left.right
    res=None
    res=FindParentNode(root,node1,node2)
    if res!=None:
        print(res.data)
    else:
        print("no parent")
