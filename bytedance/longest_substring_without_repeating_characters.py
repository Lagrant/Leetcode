class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_dict = {}
        start, end, max_l = 0, 0, 0
        for i, c in enumerate(s):
            if c not in s_dict:
                s_dict[c] = i
            else:
                if s_dict[c] >= start:
                    max_l = max(max_l, end - start)
                    start = s_dict[c] + 1
                s_dict[c] = i
            end += 1
        max_l = max(max_l, end - start)
        return max_l
    
if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("aabaab!bb"))