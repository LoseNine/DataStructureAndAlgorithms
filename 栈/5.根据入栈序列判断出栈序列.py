class Stack:
    def __init__(self):
        self.arr=[]
    def is_empty(self):
        return  self.size()==0
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
def judge_pop_push(push,pop):
    if push==None or pop==None:
        return None
    pushlen=len(push)
    poplen=len(pop)
    pushnil=0
    popnil=0
    s=Stack()
    while pushnil<pushlen:
        s.push(push[pushnil])
        pushnil+=1
        print(s.top(),pop[popnil])
        #先判断是否为空，因为最后一步nil=5会报错
        while (not s.is_empty())and (s.top()== pop[popnil]) :
            s.pop()
            popnil+=1
    return s.is_empty() and popnil==poplen

if __name__ == '__main__':
    push=[1,2,3,4,5]
    pop=[5,4,3,2,1]
    print(judge_pop_push(push,pop))
