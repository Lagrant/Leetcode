# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
import random
class Solution:
    def find_pair(self, word1, word2, num):
        cnt = 0
        for i in range(len(word1)):
            if (word1[i] == word2[i]):
                cnt += 1
                if (cnt > num):
                    return False
        if (cnt != num):
            return False
        return True

    def findSecretWord(self, wordlist, master) -> None:
        potential = wordlist
        guess_word = wordlist[random.randint(0, len(potential)-1)]
        guess = master.guess(guess_word)
        if (guess == len(guess_word)):
            return
        
        
        while True:
            poten_new = []
            for word in potential:
                if (self.find_pair(guess_word, word, guess)):
                    poten_new.append(word)
                    
            potential = poten_new
            guess_word = potential[random.randint(0, len(potential)-1)]
            guess = master.guess(guess_word)
            if (guess == len(guess_word)):
                return
