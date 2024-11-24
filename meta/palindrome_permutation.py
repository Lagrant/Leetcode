from collections import defaultdict
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        s_dict = defaultdict(int)
        for c in s:
            s_dict[c] += 1
        odd = 0
        for c, cnt in s_dict.items():
            if cnt % 2 == 1:
                odd += 1
                if odd > 1:
                    return False
        return True