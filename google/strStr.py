class Solution:
    def lengthOfLongestSubstring(self, s: str, needle: str) -> int:
        value_table = [0] * len(s)
        i, j = 0, 1
        while (j < len(needle)):
            if (needle[i] == needle[j]):
                value_table[j] = i + 1
                i += 1
                j += 1
            elif (i == 0):
                j += 1
            else:
                i = value_table[i - 1]
        
        i, j = 0, 0
        while (i < len(s)):
            if (s[i] == needle[j]):
                i += 1
                j += 1
            elif (j == 0):
                i += 1
            else:
                j = value_table[j-1]
            
            if (j == len(needle)):
                return i - j
        
        return -1

sol = Solution()
print(sol.lengthOfLongestSubstring('abcabcaab', 'cabcaa'))