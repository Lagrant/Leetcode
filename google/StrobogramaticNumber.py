class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if (len(num) == 1):
            if (num == '8' or num == '0' or num == '1'):
                return True
            else:
                return False
        for i in range(len(num) // 2 + 1):
            j = len(num) - i - 1
            if (num[i] == '6' and num[j] == '9' or num[i] == '9' and num[j] == '6'\
                or num[i] == '8' and num[j] == '8' or num[i] == '1' and num[j] == '1'\
                    or num[i] == '0' and num[j] == '0'):
                    continue
            else:
                return False
        
        return True