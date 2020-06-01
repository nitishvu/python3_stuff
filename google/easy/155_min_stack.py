
def get_min_ele(stack1):
    stack1 = sorted(stack1)
    try:
        return stack1[1]
    except:
        return None

    

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None
        self.topitem = None
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        
        if self.min == None:
            self.min = x
        elif x < self.min:
                self.min = x
            
        

    def pop(self) -> None:
        if self.stack[-1] ==self.min:
            self.min = get_min_ele(self.stack)

        self.stack.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]
        
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()