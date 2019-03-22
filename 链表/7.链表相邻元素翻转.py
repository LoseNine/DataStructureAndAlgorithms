class Node:
    def __init__(self,x):
        self.data=x
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
    def reverse_second(self):
        head=self.head
        cur=head.next
        pre=head
        next=None
        while cur!=None and cur.next!=None:
            next=cur.next.next
            pre.next=cur.next
            cur.next.next=cur
            cur.next=next
            pre=cur
            cur=next

if __name__ == '__main__':
    t=Tree()
    for i in range(6):
        t.append(i)
    #head 0 1 2 3 4 5
    #head 1 0 3 2 5 4
    t.travel()
    t.reverse_second()
    t.travel()