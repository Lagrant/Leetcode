from collections import defaultdict
class Solution:
    """
    The key difference is that the answer uses a tree to
    store word prefixes and words, I use a hash table to 
    store word prefixes and words which is space consuming.
    """
    def __init__(self) -> None:
        self.h = [defaultdict(list), defaultdict(list), defaultdict(list)]
        self.word_l = 0
    def wordSquares(self, words):
        for word in words:
            self.h[0][word[0]].append(word)
            self.h[1][word[:2]].append(word)
            self.h[2][word[:3]].append(word)
        self.word_l = len(words[0]) - 1
        if (self.word_l == 0):
            return words
        res = []
        for word in words:
            r1 = self.find_square(0, [word])
            res.extend(r1)
        return res

    def find_square(self, cnt, head):
        head_c = ''
        cnt += 1
        for h in head:
            head_c += h[cnt]
        word_lst = self.h[cnt-1][head_c]
        if (cnt == self.word_l):
            res = []
            for w in word_lst:
                res.append(head.copy())
                res[-1].append(w)
            return res
        
        res = []
        for w in word_lst:
            head.append(w)
            res1 = self.find_square(cnt, head)
            res.extend(res1)
            head = head[:cnt]
        
        return res

sol = Solution()
print(sol.wordSquares(["abaa","aaab","baaa","aaba"]))

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []
        
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        root = TrieNode()
        for word in words:
            curr = root
            for letter in word:
                curr.words.append(word)
                if letter not in curr.children:
                    curr.children[letter] = TrieNode()
                curr = curr.children[letter]
                        
        n = len(words[0])
        output = []

        def dfs(i: int, squares: List[str]):
            if i == n:
                output.append(squares[:])
                return
            
            prefix = [word[i] for word in squares]
            
            curr = root
            for letter in prefix:
                if letter not in curr.children:
                    return
                else:
                    curr = curr.children[letter]
            
            for word in curr.words:
                squares.append(word)
                dfs(i + 1, squares)
                squares.pop()
        
        dfs(0, [])
        return output