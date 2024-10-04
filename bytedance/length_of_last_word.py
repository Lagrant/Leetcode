class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')
        idx = len(s) - 1
        while s[idx] == '':
            idx -= 1
        return len(s[idx])