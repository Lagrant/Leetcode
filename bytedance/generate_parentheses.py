from collections import deque
class Solution:
    def generateParenthesis(self, n: int):
        def pair(lcnt, rcnt, parens):
            if lcnt == 0:
                for i in range(len(parens)):
                    parens[i] += ')' * rcnt
                return parens
            
            res = []
            nparens = []
            for cp in parens:
                nparens.append(cp + '(')
            res.extend(pair(lcnt - 1, rcnt, nparens))
            if rcnt > lcnt:
                nparens = []
                for cp in parens:
                    nparens.append(cp + ')')
                res.extend(pair(lcnt, rcnt - 1, nparens))
            return res

        parens = pair(n - 1, n, ['('])
        return parens
    
if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))