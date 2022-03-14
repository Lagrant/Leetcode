class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        word_map = {}
        repeat_map = {}
        for i in range(len(s)):
            if (s[i] not in word_map):
                word_map[s[i]] = t[i]
                if (t[i] in repeat_map):
                    return False
                else:
                    repeat_map[t[i]] = 1
                    
            elif (word_map[s[i]] != t[i]):
                return False
        
        return True

sol = Solution()
print(sol.isIsomorphic('badc', 'baba'))