class Stack:
    def __init__(self):
        self.items=[]
    def size(self):
        return len(self.items)
    def is_empty(self):
        return len(self.items)==0
    def push(self,x):
        self.items.append(x)
    def pop(self):
        self.items.pop()
    def top(self):
        if self.is_empty():
            return None
        return self.items[-1]

if __name__ == '__main__':
    s=Stack()
    print(s.is_empty())
    for i in range(7):
        s.push(i)
