class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Tree:
    def __init__(self):
        self.head=Node("head")
    def append(self,x):
        node=Node(x)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=node
    def travel(self):
        cur=self.head
        while cur!=None:
            print(cur.data)
            cur=cur.next
    def reverse(self):
        head=self.head
        pre=head.next
        cur=head.next.next
        pre.next=None   #就差这一步，要把一开始的指向None,吾休矣
        while cur.next!=None:
            next = cur.next
            cur.next=pre
            pre=cur
            cur=next
        cur.next=pre
        head.next=cur
    #插入法
    def reverse2(self):
        head=self.head
        cur=head.next.next
        head.next.next=None#这一步也是至关重要
        while cur!=None:
            next=cur.next
            cur.next=head.next
            head.next=cur
            cur=next


if __name__ == '__main__':
    tree=Tree()
    for i in range(5):
        tree.append(i)
    tree.travel()
    tree.reverse()
    tree.travel()
    tree.reverse2()
    tree.travel()