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
    def find_K(self,k):
        cur=self.head
        n=0
        while cur!=None:
            cur=cur.next
            n+=1
            if n==k:
                print("倒数第%d的数字为%d"%(k,cur.data))
                break
    #快慢指针法，让快的先走K个，之后等到了None#，slow就是答案
    def find_K2(self,k):
        cur=self.head
        slow=cur.next
        fast=cur.next
        for i in range(k):
            fast=fast.next
        while fast!=None:
            slow=slow.next
            fast=fast.next
        print("倒数第%d的数字为%d"%(k,slow.data))


if __name__ == '__main__':
    tree=Tree()
    for i in range(8):
        tree.append(i)
    tree.travel()
    tree.find_K2(3)
    tree.reverse()
    tree.travel()
    tree.find_K(3)
