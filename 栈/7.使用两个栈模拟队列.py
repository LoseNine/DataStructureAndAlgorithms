class Stcak:
    def __init__(self):
        self.arr=[]
    def is_empty(self):
        return len(self.arr)==0
    def size(self):
        return len(self.arr)
    def push(self,x):
        self.arr.append(x)
    def pop(self):
        if self.is_empty():
            return None
        return self.arr.pop()
    def top(self):
        if self.is_empty():
            return None
        return self.arr[-1]
class StackQueue:
    def __init__(self):
        self.spush=Stcak()
        self.spop=Stcak()
    def enQueue(self,x):
        self.spush.push(x)
    def deQueue(self):
        while not self.spush.is_empty():
            self.spop.push(self.spush.pop())
        return self.spop.pop()
if __name__ == '__main__':
    s=StackQueue()
    for i in range(5):
        s.enQueue(i)
    for i in range(5):
        print(s.deQueue())