from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        s_dict = defaultdict(list)
        for s in strs:
            s_dict[str(sorted(s))].append(s)
        return list(s_dict.values())