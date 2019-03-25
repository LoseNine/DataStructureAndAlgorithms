#空间换时间
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
class MinStack:
    def __init__(self):
        self.element=Stcak()
        #min的top总是最小值
        self.minele=Stcak()
    def push(self,x):
        self.element.push(x)
        if self.minele.is_empty():
            self.minele.push(x)
        else:
            if x<self.minele.top():
                self.minele.push(x)
    def pop(self):
        if self.element.is_empty():
            return None
        i=self.element.pop()
        if i==self.minele.top():
            self.minele.pop()
        return i
    def low(self):
        if self.minele.is_empty():
            return None
        return self.minele.top()
if __name__ == '__main__':
    s=MinStack()
    for i in range(6):
        s.push(i)
    s.push(-1)
    print(s.low())
    s.pop()
    print(s.low())






