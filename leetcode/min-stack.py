class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, y):
        self.stack.append(y)
        if self.minstack:
            self.minstack.append(min(y,self.minstack[-1]))
        else:
            self.minstack.append(y)    

    def pop(self) :
        if self.stack:
            self.stack.pop()
            self.minstack.pop()
        else:
            pass    

    def top(self) :
        if self.stack:
            return self.stack[-1]
        else:
            return -1    

    def getMin(self):
        if self.minstack:
            return self.minstack[-1]
        else:
            return -1    


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()