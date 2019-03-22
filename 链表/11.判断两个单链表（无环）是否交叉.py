
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
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

def Same(head1,head2):
    t1=head1
    t2=head2
    n1=0
    n2=0
    while t1.next!=None:
        t1=t1.next
        n1+=1
    while t2.next!=None:
        t2=t2.next
        n2+=1
    #有交叉成“Y”形状，尾部节点相同
    head1=head1.next
    head2=head2.next
    if t2.data==t1.data:
        if n1>n2:
            n=n1-n2
            while n>0:
                head1=head1.next
                n-=1
        if n1<n2:
            n=n2-n1
            while n>0:
                head2=head2.next
                n-=1
        print(head2.data)
        while head1!=head2:
            head1=head1.next
            head2=head2.next
            if head1.data==head2.data:
                print("有交叉")
                return
    else:
        print("无交叉")


if __name__ == '__main__':
    t1=Tree()
    t2=Tree()
    for i in range(4):
        t1.append(i)
    for i in range(1,10,2):
        t2.append(i)
    for i in range(8,11):
        t1.append(i)
        t2.append(i)
    t1.travel()
    print()
    t2.travel()
    Same(t1.head,t2.head)


