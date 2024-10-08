class TreeNode:
    def __init__(self) -> None:
        self._pass = 0
        self._end = 0
        self.nexts = {}
class Trie:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.nexts:
                cur.nexts[w] = TreeNode()
            cur._pass += 1
            cur = cur.nexts[w]
        cur._end += 1
        cur._pass += 1

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.nexts:
                return False
            cur = cur.nexts[w]
        return not cur._end == 0

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w not in cur.nexts:
                return False
            cur = cur.nexts[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)