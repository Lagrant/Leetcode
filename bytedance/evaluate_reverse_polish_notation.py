from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        express = []
        operators = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b, '/': divide}
        for t in tokens:
            if t not in operators:
                express.append(int(t))
                continue
            dig2 = express.pop()
            dig1 = express.pop()
            express.append(operators[t](dig1, dig2))
        return express[0]

def divide(a, b):
    if a % b == 0:
        return a // b
    return a // b if a // b >= 0 else a // b + 1

if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["4","-2","/","2","-3","-","-"]))