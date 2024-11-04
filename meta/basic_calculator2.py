from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        s = s.replace(' ', '')
        # nstack = []
        # ostack = []
        stack = deque()
        operator = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y,
        }

        while i < len(s):
            if i >= len(s):
                break
            if s[i] not in operator:
                cumi, i = self.parse_int(s, i)
                stack.append(cumi)
            elif s[i] == '+' or s[i] == '-':
                stack.append(s[i])
                i += 1
            else:
                op = s[i]
                b, i = self.parse_int(s, i + 1)
                a = stack.pop()
                stack.append(operator[op](a, b))
        while len(stack) > 1:
            a = stack.popleft()
            op = stack.popleft()
            b = stack.popleft()
            stack.appendleft(operator[op](a, b))
        return stack[0]
    
    def parse_int(self, s, i):
        cumi = ''
        while i < len(s) and '0' <= s[i] <= '9':
            cumi += s[i]
            i += 1
        return int(cumi), i
    
if __name__ == '__main__':
    s = Solution()
    print(s.calculate("3+2*2"))