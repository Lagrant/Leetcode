from typing import List
from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lengs = [len(w) for w in wordDict]
        lengs = sorted(list(set(lengs)))
        wordDict = dict(zip(wordDict, range(len(wordDict))))
        match_dict = {}
        subs = ''
        for c in s:
            subs += c
            if subs in wordDict:
                match_dict[subs] = 1
        for i in range(len(s)):
            if s[:i] not in match_dict:
                continue
            for wd in wordDict:
                match_dict[s[:i] + wd] = 1
        return s in match_dict
    
if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("applepenapple", ["apple","pen"]))