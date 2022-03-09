class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (len(s) == 0 or len(s) == 1):
            return s
        
        if (len(s) == 2):
            if (s[0] == s[1]):
                return s
            else:
                return s[0]
                
        max_len = -1
        max_palin = ''
        half_palin = ''
        for i in range(len(s)):
            half_palin = s[i]
            mid = i
            for j in range(i + 1, len(s)):
                if (half_palin == s[mid+1:j+1]):
                    if (j - i + 1 > max_len):
                        max_len = j - i + 1
                        max_palin = s[i:j+1]
                if (int((j - i + 1) / 2) + i> mid):
                    mid = int((j - i + 1) / 2) + i
                else:
                    if (mid > i):
                        half_palin = s[mid] + half_palin
        if (max_palin == ''):
            return s[0]
        return max_palin

sol = Solution()
print(sol.longestPalindrome("abccba"))
        
