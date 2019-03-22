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
        while cur.next!=None:
            print(cur.data)
            cur=cur.next
        print(cur.data)
    def delete_nosort(self):
        head=self.head
        cur=head.next
        while cur!=None:
            inner_pre=cur
            inner=cur.next
            while inner!=None:
                if cur.data==inner.data:
                    inner_pre.next=inner.next
                    inner=inner.next
                else:
                    inner_pre=inner
                    inner=inner.next
            cur=cur.next
    def delete_sort(self):
        head=self.head
        pre=head.next
        cur=pre.next
        while cur!=None:
            if pre.data==cur.data:
                pre.next=cur.next
                cur=cur.next
            else:
                pre=cur
                cur=cur.next

if __name__ == '__main__':
    tree=Tree()
    tree.append(1)
    tree.append(3)
    tree.append(5)
    tree.append(5)
    tree.append(7)
    tree.travel()
    tree.delete_sort()
    tree.travel()
