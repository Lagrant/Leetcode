class Solution:
    def calculate(self, s: str) -> int:
        express = []
        paren = []
        operators = {'+': lambda a, b: a + b, '-': lambda a, b: a - b}
        s = s.replace(' ', '')
        for i, c in enumerate(s):
            if c != ')':
                if c not in operators and c != '(':
                    if s[i - 1] == '-' and (i - 2 >= 0 and s[i - 2] == '(' or i - 1 == 0):
                        express[-1] += c
                    elif len(express) > 0 and express[-1] not in operators and express[-1] != '(':
                        express[-1] += c
                    else:
                        express.append(c)
                    continue
                if c == '(':
                    paren.append(len(express))
                express.append(c)
            else:
                idx = paren.pop()
                if express[idx + 1] == '-':
                    express[idx + 2] = -express[idx + 2]
                    substack, k = [express[idx + 2]], idx + 3
                else:
                    substack, k = [express[idx + 1]], idx + 2
                while k < len(express) - 1:
                    if express[k] not in operators:
                        substack.append(express[k])
                        k += 1
                        continue
                    dig1 = substack.pop()
                    dig2 = express[k + 1]
                    substack.append(operators[express[k]](int(dig1), int(dig2)))
                    k += 2
                express[idx] = substack[0]
                express = express[:idx + 1]
                if (len(express) > 2 and express[-3] == '(' or len(express) == 2) and express[-2] == '-':
                    express[-2] = -int(express[-1])
                    express = express[:-1]
        if express[0] == '-':
            express[1] = -int(express[1])
            express = express[1:]
        substack, k = [int(express[0])], 1
        while k < len(express) - 1:
            if express[k] not in operators:
                substack.append(int(express[k]))
                k += 1
                continue
            dig1 = substack.pop()
            dig2 = express[k + 1]
            substack.append(operators[express[k]](int(dig1), int(dig2)))
            k += 2
        return substack[0]
    
    def calculate2(self, s: str) -> int:
        stack = []
        cur = res = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                cur = cur * 10 + int(ch)
            elif ch == "+":
                res += cur * sign
                cur = 0
                sign = 1
            elif ch == "-":
                res += cur * sign
                cur = 0
                sign = -1
            elif ch == "(":
                stack.append(sign)
                stack.append(res)
                sign = 1
                res = 0
            elif ch == ")":
                res += cur * sign
                prev_res = stack.pop()
                prev_sign = stack.pop()
                res *= prev_sign
                res += prev_res
                cur = 0
        res += sign * cur
        return res

if __name__ == '__main__':
    cal = Solution()
    print(cal.calculate("-(-2)+4"))