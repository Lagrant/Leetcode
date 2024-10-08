from collections import defaultdict
from collections import deque
from re import S
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if len(wordList) == 1:
            if endWord == beginWord:
                return 1
            if endWord != wordList[0]:
                return 0
            return 2 if self.onediff(endWord, beginWord) else 0
        q = deque()
        q.append((beginWord, 1))
        visited = {beginWord:1}
        subwordlist = []
        while len(q) > 0:
            cur = q.popleft()
            if cur[0] == endWord:
                return cur[1] + 1
            for w in wordList:
                if w in visited:
                    continue
                if self.onediff(cur[0], w):
                    if w == endWord:
                        return cur[1] + 1
                    q.append((w, cur[1] + 1))
                    visited[w] = 1
                else:
                    subwordlist.append(w)
            wordList, subwordlist = subwordlist, []
            # del visited
            # visited = {}
        return 0

    def onediff(self, word1, word2):
        cnt = 0
        for w1, w2 in zip(word1, word2):
            if w1 != w2:
                cnt += 1
                if cnt > 1:
                    return False
        return cnt == 1