from typing import List
from collections import defaultdict, deque, Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ws = ''.join(words)
        if len(s) == len(ws) and s == ws:
            return [0]
        if len(s) < len(ws):
            return []
        if len(set(s)) == 1 and set(s) == set(ws):
            return list(range(len(s) - len(ws) + 1))
        
        l = len(words[0])
        s_dict = Counter(words)

        res, piv, s_size = [-1], 0, len(s) - l
        while piv < s_size:
            i = piv
            start = piv
            perm, word_cnt = defaultdict(deque), len(words)
            while i < len(s):
                ss = s[i:i + l]
                if ss not in s_dict:
                    # piv = i + l - 1
                    break
                if len(perm[ss]) < s_dict[ss]:
                    perm[ss].append(i)
                    i += l
                    word_cnt -= 1
                else:
                    if start <= perm[ss][0]:
                        word_cnt = word_cnt + (perm[ss][0] - start) //  l
                        start = perm[ss][0] + l
                    else:
                        word_cnt -= 1
                    perm[ss].popleft()
                    perm[ss].append(i)
                    i += l
                if not word_cnt:
                    res.append(start)
                    piv = start
                    break
            piv += 1
        return res[1:]



if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))