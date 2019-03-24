class Node:
    def __init__(self,x=None):
        self.data=x
        self.next=None

class Queue:
    def __init__(self):
        self.arr=Node()
    def is_empty(self):
        cur=self.arr
        if cur.next==None:
            return True
        else:
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
    def enQueue(self,x):
        node=Node(x)
        if self.is_empty():
            self.arr.next=node
            return
        cur=self.arr
        while cur.next!=None:
            cur=cur.next
        cur.next=node
    def deQueue(self):
        if self.is_empty():
            return None
        pre=self.arr
        cur=pre.next
        if cur.next!=None:
            pre.next=cur.next
        else:
            pre.next=None
    def front(self):
        if self.is_empty():
            return None
        return self.arr.next.data
    def back(self):
        if self.is_empty():
            return None
        cur=self.arr
        while cur.next!=None:
            cur=cur.next
        return cur.data
if __name__ == '__main__':
    q=Queue()
    print(q.is_empty())
    print(q.size())
    q.enQueue(1)
    q.enQueue(2)
    print(q.back())
    print(q.front())
    q.deQueue()
    print(q.is_empty())
    print(q.size())
    print(q.front(),q.front())
