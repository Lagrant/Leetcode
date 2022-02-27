class Solution:
    """
    Store chars in a dict, the key thing is that the new 
    coming char may hit (1) before the start; (2) on the 
    start; (3) after the start. Deal with these cases one
    by one.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:

        s_d = {}
        max_len = 0
        cur_len = 0
        start = 0
        for i in range(len(s)):
            if (s[i] not in s_d or s_d[s[i]] < start):
                s_d[s[i]] = i
                cur_len += 1
            elif (s_d[s[i]] == start):
                start += 1
                s_d[s[i]] = i
            else:
                if (max_len < cur_len):
                    max_len = cur_len
                cur_len -= (s_d[s[i]] - start)
                start = s_d[s[i]] + 1
                
                s_d[s[i]] = i

        return max_len if (max_len > cur_len) else cur_len

sol = Solution()
print(sol.lengthOfLongestSubstring('abba'))