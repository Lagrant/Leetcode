class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)
        num1 = list(map(lambda x: int(x), num1))
        num2 = list(map(lambda x: int(x), num2))
        i, j = len(num1) - 1, len(num2) - 1
        addi = 0
        res = []
        while i >= 0 and j >= 0:
            dig = num1[i] + num2[j] + addi
            if dig > 9:
                addi = 1
                dig -= 10
            else:
                addi = 0
            res.append(dig)
            i -= 1
            j -= 1

        while i >= 0:
            dig = num1[i] + addi
            if dig > 9:
                addi = 1
                dig -= 10
            else:
                addi = 0
            res.append(dig)
            i -= 1
        while j >= 0:
            dig = num2[j] + addi
            if dig > 9:
                addi = 1
                dig -= 10
            else:
                addi = 0
            res.append(dig)
            j -= 1
        
        if addi == 1:
            res.append(addi)
        
        multi = ''.join(map(lambda x: str(x), res[::-1]))
        return multi

if __name__ == '__main__':
    s = Solution()
    print(s.addStrings('11', '123'))