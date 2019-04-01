class Node:
    def __init__(self):
        self.data=None
        self.left=None
        self.right=None
def FindRoad(root,num,sums,v):
    sums+=root.data
    v.append(sums)
    if root.left==None and root.right==None and num==sums:
        i=0
        while i<len(v):
            print(v[i])
            i+=1
        print('\n')
    if root.left!=None:
        FindRoad(root.left,num,sums,v)
    if root.right!=None:
        FindRoad(root.right, num, sums, v)
    sums-=v[-1]
    v.remove(v[-1])
def constructTree():
    root=Node()
    node1=Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    root.data=6
    node1.data=3
    node2.data=-7
    node3.data=-1
    node4.data=9
    root.left=node1
    root.right=node2
    node1.left=node3
    node2.right=node4
    return root
if __name__ == '__main__':
    root=constructTree()
    s=[]
    print("path is:")
    FindRoad(root,8,0,s)