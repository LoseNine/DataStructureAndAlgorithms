class Node:
    def __init__(self,x=None):
        self.data=x
        self.next=None

class Tree:
    def __init__(self):
        self._head=Node("head")
    def append(self,x):
        node=Node(x)
        cur=self._head
        while cur.next!=None:
            cur=cur.next
        cur.next=node
    def travel(self):
        cur=self._head
        while cur!=None:
            print(cur.data)
            cur=cur.next
def adds(x,y):
    t1=x.next
    t2=y.next
    c=0#进位
    t=Tree()
    while t1!=None and t2!=None:
        data=t1.data+t2.data+c
        sum=data%10#个位
        c=data//10#十位
        t1=t1.next
        t2=t2.next
        t.append(sum)
    if t1==None and t2!=None:
        while t2!=None:
            data=t2.data+c
            sum=data%10
            c=data//10
            t2=t2.next
            t.append(sum)
    if t2==None and t1!=None:
        while t1!=None:
            data=t1.data+c
            sum=data%10
            c=data//10
            t1=t1.next
            t.append(sum)
    if c!=0:
        t.append(c)
    t.travel()


if __name__ == '__main__':
    tree1=Tree()
    tree1.append(3)
    tree1.append(1)
    tree1.append(5)
    tree1.append(3)
    tree2=Tree()
    tree2.append(4)
    tree2.append(9)
    tree2.append(6)

    adds(tree1._head,tree2._head)
