class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        n, ans = len(s), 0

        def palin(left, right):
            cnt = 0
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                cnt += 1
            return cnt
        
        for i in range(n):
            even = palin(i, i + 1)
            odd = palin(i, i)
            ans += even + odd
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.countSubstrings('abccbabba'))