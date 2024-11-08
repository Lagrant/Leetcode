class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) == 0 or stack[-1] != c:
                stack.append(c)
            elif c == stack[-1]:
                stack.pop()
        return ''.join(stack)