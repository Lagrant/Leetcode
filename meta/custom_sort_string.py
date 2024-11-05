from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_dict = defaultdict(int)
        for c in s:
            s_dict[c] += 1
        perm_s = ''
        for c in order:
            if c in s_dict:
                perm_s += c * s_dict[c]
                del s_dict[c]
        for c in s_dict:
            perm_s += c * s_dict[c]
        return perm_s