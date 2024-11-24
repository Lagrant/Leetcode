class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = {'a':1, 'e': 1, 'i': 1, 'o':1, 'u': 1, 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1}
        words = sentence.split(' ')
        
        for i, word in enumerate(words):
            if word[0] in vowel:
                word += 'ma' + (i + 1) * 'a'
            else:
                word = word[1:] + word[0] + 'ma' + (i + 1) * 'a'
            words[i] = word
        return ' '.join(words)