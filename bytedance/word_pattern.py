class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pm, sm = {}, {}
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        for p, c in zip(pattern, s):
            if p not in pm:
                if c in sm:
                    return False
                pm[p] = c
                sm[c] = p
            if pm[p] != c:
                return False
        return True