class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (len(s) == 0):
            return ''

        start, end = 0, 0
        for i in range(len(s)):
            l1 = self.expend(s, i, i)
            l2 = self.expend(s, i, i + 1)
            max_l = max(l1, l2)
            if (max_l > end - start):
                start = i - (max_l - 1) // 2
                end = i + max_l // 2
        return s[start:end + 1]
    
    def expend(self, s, left, right):
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1