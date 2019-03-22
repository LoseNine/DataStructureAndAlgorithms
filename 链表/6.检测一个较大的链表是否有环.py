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
    def last(self):
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        return cur

def judge_circle(head):
    slow=head
    fast=head
    while fast.next!=None and fast!=None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            print("链表有环")
            return slow
    print("无环")
def find_node(head,meetnode):
    first=head
    second=meetnode
    while first!=second:
        first=first.next
        second=second.next
    return first

#01  13  25  34 43  55
if __name__ == '__main__':
    t=Tree()
    for i in range(6):
        t.append(i)
    last=t.last()
    last.next=t.head.next.next.next.next
    #t.travel()
    meetNode=judge_circle(t.head)
    loopNode=find_node(t.head,meetNode)
    print("入环口：",loopNode.data)