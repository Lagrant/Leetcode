from sympy import sec


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dig_map = {}
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            if (secret[i] == guess[i]):
                bulls += 1
        
        for c in secret:
            dig_map[c] = dig_map.get(c, 0) + 1
        
        for c in guess:
            if (c in dig_map and dig_map[c] > 0):
                cows += 1
                dig_map[c] -= 1
        
        cows -= bulls

        return str(bulls) + 'A' + str(cows) + 'B'