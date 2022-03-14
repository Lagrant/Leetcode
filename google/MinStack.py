class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        if (self.min_val > val):
            self.min_val = val
        self.stack.append(val)

    def pop(self) -> None:
        if (len(self.stack) == 0):
            return
        
        k = self.stack.pop()
        if (k != self.min_val):
            return
        if (len(self.stack) == 0):
            self.min_val = float('inf')
        else:
            self.min_val = min(self.stack)

    def top(self) -> int:
        # if (len(self.stack) == 0):
        #     return None
        
        return self.stack[-1]

    def getMin(self) -> int:
        
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif self.min_stack[-1] > val:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]