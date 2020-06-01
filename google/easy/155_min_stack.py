class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max =  0
        self.min = 0
        

    def push(self, x: int) -> None:
        if self.stack ==[]:
            self.min = x
            self.max = x
            self.stack.append(x)
            
        if x <=self.min:
            self.min = x
        else:
            self.max = x
        self.stack.append(x)
        
        #print(self.stack)

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.max
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
x=2
obj = MinStack()
obj.push(x)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()