class User:
    def __init__(self,n,name):
        self.n=n
        self.name=name
    def setn(self,n):
        self.n=n
    def __str__(self):
        return str("id:%s name:%s"%(self.n,self.name))
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
class System:
    def __init__(self):
        self.stack=Stcak()
    def spush(self,x):
        self.stack.push(x)
    def spop(self):
        self.stack.pop()
        self.update()
    def randompop(self):
        self.stack.arr.pop(2)
        self.update()
    def update(self):
        n=1
        for i in self.stack.arr:
            i.setn(n)
            n+=1
    def travel(self):
        for i in self.stack.arr:
            print(i)
if __name__ == '__main__':
    s=System()
    s2=User(2, "alice2")
    s.spush(User(1,"alice"))
    s.spush(s2)
    s.spush(User(3, "alice3"))
    s.spush(User(4, "alice4"))
    s.spush(User(5, "alice5"))
    s.travel()
    s.spop()
    s.travel()
    s.randompop()
    s.travel()
