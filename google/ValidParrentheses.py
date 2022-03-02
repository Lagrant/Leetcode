class Solution:
    def isValid(self, s: str) -> bool:
        parens = []
        right = {')': '(', '}': '{', ']': '['}
        for p in s:
            if (p in right and (len(parens) == 0 or parens[-1] != right[p])):
                return False
            if (p in right and right[p] == parens[-1]):
                parens.pop()
            else:
                parens.append(p)
        
        return False if (len(parens) > 0) else True

sol = Solution()
print(sol.isValid("(]"))
        