class Node:
    def __init__(self):
        self.data=None
        self.left=None
        self.right=None
#中序遍历
def printTree(root):
    if root==None:
        return
    if root.left!=None:
        printTree(root.left)
    print(root.data)
    if root.right!=None:
        printTree(root.right)
def createDupTree(root):
    if root==None:
        return
    dupTree=Node()
    dupTree.data=root.data
    dupTree.left=createDupTree(root.left)
    dupTree.right=createDupTree(root.right)
    return dupTree