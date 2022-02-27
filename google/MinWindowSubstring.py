class Solution:
    def shrink(self, pos, l, r, max_str):
        max_len = len(max_str)
        r1 = len(pos)
        dic_cnt = {}
        cnt = 0
        for i in range(r+1, r1):
            if (pos[i][0] not in dic_cnt):
                dic_cnt[pos[i][0]] = 1

            else:
                dic_cnt[pos[i][0]] += 1
            

    def minWindow(self, s: str, t: str) -> str:
        dic_t = {}
        t_cnt = len(t)
        for i in t:
            dic_t[i] = dic_t.get(i, 0) + 1
        l = r = 0
        max_len = 0
        max_str = ""
        pos = []

        for i, c in enumerate(s):
            if (c not in dic_t):
                continue
            pos.append([c, i])
            if (t_cnt > 0 and dic_t[c] > 0):
                t_cnt -= 1
                dic_t[c] -= 1
            if (t_cnt == 0):
                l = 0
                r = len(pos) - 1
                max_len = pos[r][1] - pos[l][1] + 1
                max_str = s[:max_len]
                break
        
        for i in range(r+1, len(s)):
            if (s[i] not in dic_t):
                continue
            pos.append([s[i], i])
            if (s[i] == s[l]):
                self.shrink(pos, l, r, max_str)


class Solution:
    """
    use two pointers on the array
    count all the chars from left to right
    decrease by one if redundant
    """
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        word, target = {}, {}
        for i in t:
            target[i] = target.get(i, 0) + 1
        
        have, need, i = 0, len(target), 0
        res, cnt = [-1, -1], float("inf")
        
        for j, ch in enumerate(s):
            word[ch] = word.get(ch, 0) + 1
            if ch in target and word[ch] == target[ch]:
                have += 1
            while have == need:
                if (j-i+1) < cnt:
                    cnt = j-i+1
                    res = [i, j]
                word[s[i]] -= 1
                if s[i] in target and word[s[i]] < target[s[i]]:
                    have -= 1
                i += 1
        
        return s[res[0]:res[1]+1]