class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sm, tm = {}, {}
        s, t = list(s), list(t)
        for i, j in zip(s, t):
            if i not in sm:
                if j in tm:
                    return False
                sm[i] = j
                tm[j] = i
            if sm[i] != j:
                return False
        return True