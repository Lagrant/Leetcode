from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if len(stack) == 0:
                stack.append(ast)
                continue
            if not (self.sign(ast) == -1 and self.sign(stack[-1]) == 1):
                stack.append(ast)
            else:
                while len(stack) > 0 and abs(ast) > abs(stack[-1]) and self.sign(ast) == -1 and self.sign(stack[-1]) == 1:
                    stack.pop()
                if len(stack) == 0 or not (self.sign(ast) == -1 and self.sign(stack[-1]) == 1):
                    stack.append(ast)
                    continue

                if abs(ast) == abs(stack[-1]):
                    stack.pop()
                
        return stack

    def sign(self, num):
        return 1 if num > 0 else -1