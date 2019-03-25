from collections import deque
#使用一个双端列表实现
class LRU:
    def __init__(self,cache):
        self.cache=cache
        self.queue=deque()
        self.hashset=set()
    def isFull(self):
        return len(self.queue)==self.cache
    def enqueue(self,x):
        if self.isFull():
            self.hashset.remove(self.queue[-1])
            self.queue.pop()
        self.queue.appendleft(x)
        self.hashset.add(x)
    def accessN(self,x):
        if x not in self.hashset:
            self.enqueue(x)
        elif x!=self.queue[0]:
            self.queue.remove(x)
            self.queue.appendleft(x)
    def printQueue(self):
        while len(self.queue)>0:
            print(self.queue.popleft())

if __name__ == '__main__':
    s=LRU(3)
    s.accessN(1)
    s.accessN(2)
    s.accessN(4)
    s.accessN(1)
    s.accessN(6)
    s.accessN(7)
    s.printQueue()