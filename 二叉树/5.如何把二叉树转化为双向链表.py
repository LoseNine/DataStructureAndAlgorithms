class Node:
    def __init__(self,x=None):
        self.data=x
        self.left=None
        self.right=None

class Test:
    def __init__(self):
        self.phead=None
        self.pend=None
    def arrayTotree(self,arr,start,end):
        root=None
        if end>=start:
            root=Node()
            mid=(start+end+1)//2
            root.data=arr[mid]
            root.left=self.arrayTotree(arr,start,mid-1)
            root.right=self.arrayTotree(arr,mid+1,end)
        else:return None
        return root

    def inOrderBSTree(self,root):
        if root==None:
            return
        #改进中序遍历
        self.inOrderBSTree(root.left)

        root.left=self.pend
        if self.phead==None:
            self.phead=root
        else:
            self.pend.right=root
        self.pend=root

        self.inOrderBSTree(root.right)








