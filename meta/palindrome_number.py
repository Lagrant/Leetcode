class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        sx = str(x)
        piv = len(sx) // 2
        for i in range(piv):
            if sx[i] != sx[-i - 1]:
                return False
        return True