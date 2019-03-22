class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

#对不带头的链表进行翻转
def Reverse(head):
    pre=head
    cur=head.next
    pre.next=None
    while cur.next!=None:
        next=cur.next
        cur.next=pre
        pre=cur
        cur=next
    cur.next=pre
    return cur

def Reverse_K(head,k):
    pre=head
    start=pre.next
    end=None
    end_next=None
    while start!=None:
        end=start
        for i in range(k-1):
            if end.next!=None:
                end=end.next
            else:
                return
        end_next=end.next
        end.next=None
        pre.next=Reverse(start)
        start.next=end_next
        pre=start
        start=end_next

class Tree:
    def __init__(self):
        self.head=Node("head")
    def append(self,x):
        node=Node(x)
        if not self.head:
            self.head=node
            return
        head=self.head
        while head.next!=None:
            head=head.next
        head.next=node
    def travel(self):
        cur=self.head
        while cur!=None:
            print(cur.data)
            cur=cur.next

if __name__ == '__main__':
    t=Tree()
    for i in range(7):
        t.append(i)
    t.travel()
    print("--------")
    Reverse_K(t.head,3)
    t.travel()