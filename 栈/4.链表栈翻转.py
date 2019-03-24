class Node:
    def __init__(self,x=None):
        self.data=x
        self.next=None

class Stack:
    def __init__(self):
        self.arr=Node()
    def is_empty(self):
        if self.arr.next==None:
            return True
        return False
    def size(self):
        if self.is_empty():
            return 0
        cur=self.arr
        i=0
        while cur.next!=None:
            cur=cur.next
            i+=1
        return i
    def push(self,x):
        node=Node(x)
        if self.is_empty():
            self.arr.next=node
            return
        cur=self.arr
        while cur.next!=None:
            cur=cur.next
        cur.next=node
    def pop(self):
        if self.is_empty():
            return None
        pre=self.arr
        cur=pre.next
        while cur.next!=None:
            pre=cur
            cur=cur.next
        pre.next=None
        return cur
    def reverse(self):
        if self.is_empty():
            return None
        head=self.arr
        pre=self.arr
        cur=pre.next
        pre=cur
        cur=pre.next
        pre.next=None
        while cur.next!=None:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        cur.next=pre
        head.next=cur
    def travel(self):
        if self.is_empty():
            return None
        cur=self.arr.next
        while cur!=None:
            print(cur.data)
            cur=cur.next


if __name__ == '__main__':
    s=Stack()
    for i in range(5):
        s.push(i)
    s.travel()
    s.reverse()
    s.travel()