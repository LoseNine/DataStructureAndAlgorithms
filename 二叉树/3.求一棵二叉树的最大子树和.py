class Node:
    def __init__(self,x=None):
        self.data=x
        self.left=None
        self.right=None

class Test:
    def __init__(self):
        self.maxSum=-2**31
    def FindMaxSubTree(self,root,maxRoot):
        if root==None:
            return 0
        lmax=self.FindMaxSubTree(root.left,maxRoot)
        rmax=self.FindMaxSubTree(root.right,maxRoot)
        sums=lmax+rmax+root.data
        if sums>self.maxSum:
            self.maxSum=sums
            maxRoot.data=root.data
        return sums

if __name__ == '__main__':
    root=Node()
    root1=Node()
    root2 = Node()
    root3 = Node()
    root4 = Node()
    root.data=6
    root1.data=3
    root2.data=-7
    root3.data=-1
    root4.data=9
    root.left=root1
    root.right=root2
    root1.left=root3
    root1.right=root4

    test=Test()
    maxRoot=Node()
    test.FindMaxSubTree(root,maxRoot)
    print(test.maxSum)
    print(maxRoot.data)