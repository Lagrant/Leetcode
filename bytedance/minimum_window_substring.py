from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if len(s) == len(t):
            return s if Counter(s) == Counter(t) else ""
        start, end = 0, 0
        tc, sc = Counter(t), defaultdict(int)
        minL, mins = 1e6, ""
        reach_cnt, t_cnt = 0, len(tc.items())
        while end < len(s):
            if s[start] not in tc:
                start += 1
            if s[end] not in tc:
                end += 1
                continue
            if sc[s[end]] < tc[s[end]]:
                sc[s[end]] += 1
                if sc[s[end]] == tc[s[end]]:
                    reach_cnt += 1
                if reach_cnt == t_cnt and end - start + 1 < minL:
                    minL = end - start + 1
                    mins = s[start: end + 1]
            else:
                cnt = 0
                scnt = start
                sc[s[end]] += 1
                while scnt < end and (s[scnt] not in tc or sc[s[scnt]] > tc[s[scnt]]):
                    cnt += 1
                    if s[scnt] in tc and sc[s[scnt]] > tc[s[scnt]]:
                        sc[s[scnt]] -= 1
                    scnt += 1
                if reach_cnt == t_cnt and end - scnt + 1 < minL:
                    minL = end - scnt + 1
                    mins = s[scnt: end + 1]
                start = scnt
            end += 1
        
        end = len(s) - 1 if end >= len(s) else end
        if end + 1 - start < len(t) or reach_cnt < t_cnt:
            return ""
        mins = s[start: end + 1] if minL > end + 1 - start else mins
        return mins

if __name__ == '__main__':
    so = Solution()
    print(so.minWindow("baab", "bbb"))