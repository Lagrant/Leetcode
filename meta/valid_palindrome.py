class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True
        return self.match(s, 0)

    def match(self, s, delcnt):
        if len(s) <= 1:
            return True
        if len(s) == 2:
            if s[0] == s[1]:
                return True
            return delcnt == 0
        i, j = 0, len(s) - 1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        if i >= j:
            return True
        
        if delcnt != 0:
            return False
            
        s = s[i:j + 1]
        if s[1] == s[-1]:
            flag = self.match(s[2: -1], 1)
            if flag:
                return True
        if s[0] == s[-2]:
            return self.match(s[1: -2], 1)
        return False
    
if __name__ == '__main__':
    s = Solution()
    print(s.validPalindrome("deeee"))