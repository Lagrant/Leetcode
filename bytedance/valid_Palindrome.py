import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        piv = len(s) // 2
        for i in range(piv):
            if s[i] != s[-i - 1]:
                return False
        return True
