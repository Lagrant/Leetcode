from typing import List
from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        match_dict = defaultdict(list)
    
        for stri in strings:
            s = list(stri)
            gap = ord(s[0])
            s_d = [(ord(c) - gap) % 26 for c in s]
            shift_s = ''
            for c in s_d:
                shift_s += chr(c)
            match_dict[shift_s].append(stri)
        return list(match_dict.values())