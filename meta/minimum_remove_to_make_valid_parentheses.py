class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if len(s) == 1:
            return '' if s == '(' or s == ')' else s
            
        pstack = []
        sval = ''
        for c in s:
            if c != '(' and c != ')':
                sval += c
            elif c == '(':
                pstack.append(len(sval))
                sval += c
            elif len(pstack) != 0:
                pstack.pop()
                sval += c
        
        if len(pstack) > 0:
            for idx in pstack[::-1]:
                sval = sval[:idx] + sval[idx + 1:]
        return sval