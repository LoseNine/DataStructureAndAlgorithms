class Queue:
    def __init__(self):
        self.arr=[]
    def is_empty(self):
        return self.size()==0
    def size(self):
        return len(self.arr)
    def enQueue(self,x):
        self.arr.append(x)
    def deQueue(self):
        if self.is_empty():
            return None
        return self.arr.pop(0)
    def front(self):
        if self.is_empty():
            return None
        return self.arr[0]
    def back(self):
        if self.is_empty():
            return None
        return self.arr[-1]
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
