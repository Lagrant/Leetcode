class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        opendict = {'(': ')', '{': '}', '[': ']'}
        closedict = {')': '(', '}': '{', ']': '['}
        matchlst = []
        for c in s:
            if c in opendict:
                matchlst.append(c)
            else:
                if len(matchlst) == 0:
                    return False
                if matchlst[-1] == closedict[c]:
                    matchlst.pop()
                else:
                    return False
        return not len(matchlst) > 0