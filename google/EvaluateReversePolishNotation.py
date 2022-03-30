from collections import deque
class Solution:
    def evalRPN(self, tokens) -> int:
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y if x // y >= 0 else x // y if x % y == 0 else x // y + 1
        }
        operands = deque([])
        for t in tokens:
            if t not in operators:
                operands.append(t)
            else:
                y = int(operands.pop())
                x = int(operands.pop())
                operands.append(str(operators[t](x, y)))
        
        return operands[0]

sol = Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))