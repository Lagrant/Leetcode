from collections import deque
class Solution:
    def generateParenthesis(self, n: int):
        def pair(stack, cnt):
            if (cnt < n):
                stack.append('(')
                parens.append('(')
                pair(stack, cnt + 1)
                stack.pop()
                parens.pop()
            if (len(stack) > 0):
                k = stack.pop()
                parens.append(')')
                pair(stack, cnt)
                stack.append(k)
                parens.pop()
            if (cnt == n and len(stack) == 0):
                comb.append(''.join(parens))
            
        stack = deque([])
        parens = []
        comb = []
        pair(stack, 0)
        
        return comb

sol = Solution()
print(sol.generateParenthesis(3))