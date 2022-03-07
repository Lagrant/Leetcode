class Solution:
    def letterCombinations(self, digits: str):
        def comb_letters(letters, dig):
            # if (len(letters) == 0):
            #     letters = digit_table[dig].copy()
            #     return
            dig_letters = digit_table[dig]
            cp_letters = letters.copy()
            for i in range(len(letters)):
                letters[i] = ''.join([letters[i], dig_letters[0]])
            for i in range(1, len(dig_letters)):
                for l in cp_letters:
                    letters.append(''.join([l, dig_letters[i]]))
            

        if (len(digits) == 0):
            return []
        
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

        letters = digit_table[digits[0]].copy()
        for i in range(1, len(digits)):
            comb_letters(letters, digits[i])

        return letters

sol = Solution()
print(sol.letterCombinations('4357'))