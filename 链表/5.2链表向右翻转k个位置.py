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
    def reverse(self):
        head=self.head
        pre=head.next
        cur=pre.next
        pre.next=None
        while cur.next!=None:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        cur.next=pre
        head.next=cur
        return self.head
    def reverse_k(self,k):
        head=self.head
        cur=head.next
        slowpre=head
        slow=head
        fastpre=head
        fast=head
        for i in range(k):
            fast=fast.next
        while fast!=None:
            slowpre=slow
            slow=slow.next
            fastpre=fast
            fast=fast.next
        slowpre.next=None
        head.next=slow
        fastpre.next=cur


if __name__ == '__main__':
    t=Tree()
    for i in range(7):
        t.append(i)
    t.travel()
    t.reverse_k(3)
    t.travel()