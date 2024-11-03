class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if len(s) == 1:
            return '' if s == '(' or s == ')' else s
            
        pstack = []
        sval = ''
        rskip = 0
        for i, c in enumerate(s):
            if c != '(' and c != ')':
                sval += c
            elif c == '(':
                pstack.append(i - rskip)
                sval += c
            else:
                if len(pstack) == 0:
                    rskip += 1
                    continue
                pstack.pop()
                sval += c
        
        if len(pstack) > 0:
            for idx in pstack[::-1]:
                sval = sval[:idx] + sval[idx + 1:]
        return sval