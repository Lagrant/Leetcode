class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w = ''
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            w = w + word1[i] + word2[j]
            i += 1
            j += 1
        if i < len(word1):
            w += word1[i:]
            return w
        if j < len(word2):
            w += word2[j:]
            return w
        return w