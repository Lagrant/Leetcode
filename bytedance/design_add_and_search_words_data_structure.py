class TreeNode:
    def __init__(self) -> None:
        self._pass = 0
        self._end = 0
        self.nexts = {}
class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.nexts:
                cur.nexts[w] = TreeNode()
            cur._pass += 1
            cur = cur.nexts[w]
        cur._end += 1
        cur._pass += 1

    def search(self, word: str) -> bool:
        def general(root, word):
            cur = root
            for i, w in enumerate(word):
                if w != '.':
                    if w not in cur.nexts:
                        return False
                    cur = cur.nexts[w]
                if w == '.':
                    for nc in cur.nexts:
                        res = general(cur.nexts[nc], word[i + 1:])
                        if res:
                            return True
                    return False
            return not cur._end == 0
        cur = self.root
        return general(cur, word)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)