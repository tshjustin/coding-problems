class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        
        # if the stack is empty, then we define the min element as the cur element 
        # update this as we go 

        # with this, all the smaller elements below the current smallest technically is still small until the smallest is popped
        if not self.stack: 
            min_val = val

        else: 
            # we found a smaller element 
            if val < self.stack[-1][1]: 
                min_val = val 
            
            else: 
                min_val = self.stack[-1][1]

        self.stack.append((val, min_val)) 


    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()