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
    def delete_node(self, node):
        if node.next!=None:
            tmp=node.next
            node.data=tmp.data
            node.next=tmp.next
        else:
            node=None
if __name__ == '__main__':
    t=Tree()
    for i in range(6):
        t.append(i)
    t.travel()
    node=t.head.next.next.next
    t.delete_node(node)
    t.travel()

