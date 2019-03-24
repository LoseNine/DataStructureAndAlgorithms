class Stack:
    def __init__(self):self.arr=[]
    def is_empty(self):
        return self.size()==0
    def size(self):
        return len(self.arr)
    def push(self,x):
        self.arr.append(x)
    def pop(self):
        self.arr.pop()
    def reverse(self):
        self.arr=self.arr[::-1]
    def travel(self):
        if self.is_empty():
            return None
        for i in self.arr:
            print(i,end=" ")
if __name__ == '__main__':
    s=Stack()
    for i in range(5):
        s.push(i)
    s.travel()
    s.reverse()
    s.travel()