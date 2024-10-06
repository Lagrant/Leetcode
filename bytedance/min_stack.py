class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_ptr = None
        self.min_val = 1e20

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min_val:
            self.min_stack.append(self.min_ptr)
            self.min_ptr = len(self.stack) - 1
            self.min_val = val
        
    def pop(self) -> None:
        if len(self.stack) == self.min_ptr + 1:
            self.min_ptr = self.min_stack.pop()
            self.min_val = self.stack[self.min_ptr] if self.min_ptr is not None else 1e20
            self.stack.pop()
        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()