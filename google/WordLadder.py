from collections import defaultdict
from collections import deque
from re import S
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        
        word_graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                word_graph[word[:i] + '*' + word[i+1:]].append(word)
        
        word_que = deque([(beginWord, 1)])
        visited = {beginWord: True}
        while(len(word_que) > 0):
            cur_word = word_que.popleft()
            for i in range(len(cur_word[0])):
                star_cur_word = cur_word[0][:i] + '*' + cur_word[0][i+1:]
                for nxt_word in word_graph[star_cur_word]:
                    if (nxt_word == endWord):
                        return cur_word[1] + 1
                    elif (nxt_word not in visited):
                        visited[nxt_word] = True
                        word_que.append((nxt_word, cur_word[1] + 1))

                word_graph[star_cur_word] = []
        
        return 0

sol = Solution()
print(sol.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))