class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = r = 0
        distinc = 0
        dic_s = {}
        sub_len = 0
        for i, c in enumerate(s):
            if (c not in dic_s or dic_s[c] == 0):
                distinc += 1
            dic_s[c] = dic_s.get(c, 0) + 1
            r = i
            
            
            while (distinc > 2):
                dic_s[s[l]] -= 1
                if (dic_s[s[l]] == 0):
                    distinc -= 1
                
                sub_len = r - l if (r - l > sub_len) else sub_len
                l += 1
        if (distinc <= 2):
            sub_len = r - l + 1 if (r - l + 1 > sub_len) else sub_len
        return sub_len

sol = Solution()
print(sol.lengthOfLongestSubstringTwoDistinct("eceba"))