class Node:
    def __init__(self,x=None):
        self.data=x
        self.next=None
class Stack:
    def __init__(self):
        self.items=Node("head")
    def is_empty(self):
        if self.items.next==None:
            return True
        else:
            return False
    def size(self):
        if self.is_empty():
            return None
        cur=self.items
        i=0
        while cur.next!=None:
            cur=cur.next
            i+=1
        return i
    def push(self,x):
        node=Node(x)
        if self.is_empty():
            self.items.next=node
        else:
            cur=self.items
            while cur.next!=None:
                cur=cur.next
            cur.next=node
    def pop(self):
        if self.is_empty():
            return None
        else:
            pre=self.items
            cur=pre.next
            while cur.next!=None:
                pre=cur
                cur=cur.next
            pre.next=None
            cur=None
    def top(self):
        if self.is_empty():
            return None
        cur=self.items
        while cur.next!=None:
            cur=cur.next
        return cur.data


if __name__ == '__main__':
    s=Stack()
    print(s.is_empty())
    print(s.size())
    s.push(1)
    s.push(2)
    print(s.is_empty())
    print(s.size())
    s.push(1)
    s.push(2)
    print(s.top())
    print(s.is_empty())
    print(s.size())
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    print(s.is_empty())
    print(s.size())
    print(s.top())

