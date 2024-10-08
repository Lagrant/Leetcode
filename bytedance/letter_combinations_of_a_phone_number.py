from typing import List
class Solution:
    def letterCombinations(self, digits: str):
        def combo(letters, digi):
            cpletters = letters.copy()
            for i in range(len(letters)):
                letters[i] += digi[0]
            for i in range(1, len(digi)):
                for cl in cpletters:
                    letters.append(f'{cl}{digi[i]}')

        
        digit_table = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return digit_table[digits]
        digits = list(digits)
        digs_l = []
        for d in digits:
            digs_l.append(digit_table[d])
        
        letters = digs_l[0].copy()
        for i in range(1, len(digs_l)):
            combo(letters, digs_l[i])
        return letters

    def letterCombinations2(self, digits: str) -> List[str]:
        numLetter = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']        
        }
        res = []
        n = len(digits)
        if n == 0:
            return []
        def backtrack(cur_res, idx):
            if idx == n:
                res.append(''.join(cur_res))
                return
            for c in numLetter[digits[idx]]:
                cur_res.append(c)
                backtrack(cur_res, idx + 1)
                cur_res.pop()
        
        backtrack([], 0)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('22'))