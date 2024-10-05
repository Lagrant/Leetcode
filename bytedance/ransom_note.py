from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc, mc = Counter(ransomNote), Counter(magazine)
        for c in rc:
            if c not in mc or rc[c] > mc[c]:
                return False
        return True