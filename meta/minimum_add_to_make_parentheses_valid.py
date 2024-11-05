class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s) == 1:
            return 1
        stack = 0
        add_cnt = 0
        for c in s:
            if c == '(':
                stack += 1
            elif stack > 0:
                stack -= 1
            else:
                add_cnt += 1
        add_cnt += stack
        return add_cnt