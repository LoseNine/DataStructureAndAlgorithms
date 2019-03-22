class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

def FindMiddleNode(head):
    if head.next==None:
        return
    slowpre=head.next
    slow=head.next
    fast=head.next
    while fast is not None and fast.next!=None:
        slowpre=slow
        slow=slowpre.next
        fast=fast.next.next
    slowpre.next=None
    return slow

def Reverse(head):
    pre=head
    cur=head.next
    head.next=None
    while cur.next!=None:
        next=cur.next
        cur.next=pre
        pre=cur
        cur=next
    cur.next=pre
    return cur

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
if __name__ == '__main__':
    t=Tree()
    t.append(1)
    t.append(2)
    t.append(3)
    t.append(4)
    t.append(5)
    t.append(6)
    t.travel()
    t2=FindMiddleNode(t.head)
    cur2=Reverse(t2)
    # while t3!=None:
    #     print(t3.data)
    #     t3=t3.next
    cur=t.head
    while cur.next!=None:
        tmp=cur.next
        cur.next=cur2
        cur=tmp
        tmp=cur2.next
        cur2.next=cur
        cur2=tmp
    cur.next=cur2
    cur=t.head
    while cur!=None:
        print(cur.data)
        cur=cur.next






