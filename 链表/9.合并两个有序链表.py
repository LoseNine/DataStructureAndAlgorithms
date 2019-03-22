class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

def merge(head1,head2):
    cur1=head1.next
    cur2=head2.next
    t=Tree()
    while cur1 and cur2:
        if cur1.data>cur2.data:
            t.append(cur2.data)
            cur2=cur2.next
        elif cur1.data<cur2.data:
            t.append(cur1.data)
            cur1=cur1.next
        elif cur1.data==cur2.data:
            t.append(cur1.data)
            t.append(cur2.data)
            cur1 = cur1.next
            cur2 = cur2.next
    if cur1 is None and cur2!=None:
        while cur2!=None:
            t.append(cur2.data)
            cur2=cur2.next
    if cur2 is None and cur1!=None:
        while cur1!=None:
            t.append(cur1.data)
            cur1=cur1.next
    return t

class Tree:
    def __init__(self):
        self.head=Node("head")
    def append(self,x):
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=Node(x)
    def travel(self):
        cur=self.head
        while cur!=None:
            print(cur.data,end=" ")
            cur=cur.next

if __name__ == '__main__':
    t1=Tree()
    t2=Tree()
    t1.append(1)
    t1.append(3)
    t1.append(4)
    t1.append(7)
    t2.append(2)
    t2.append(4)
    t2.append(5)
    t2.append(6)
    t2.append(9)
    t1.travel()
    print()
    t2.travel()
    t=merge(t1.head,t2.head)
    print()
    t.travel()