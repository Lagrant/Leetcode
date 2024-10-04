from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        deriv = [None] * len(ratings)
        candies = [0] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                deriv[i] = 1
            elif ratings[i] == ratings[i - 1]:
                deriv[i] = 0
            else:
                deriv[i] = -1
        localmins = self.findlocalmins(deriv)
        for i, lm in enumerate(localmins):
            self.to_the_left(deriv, candies, lm)
            self.to_the_right(deriv, candies, lm)
        return sum(candies)
    
    def to_the_left(self, deriv, candies, idx):
        if deriv[idx] == 0:
            candies[idx] = 1
            return
        candies[idx] = 1
        idx -= 1
        while idx >= 0 and deriv[idx + 1] == -1:
            candies[idx] = max(candies[idx], candies[idx + 1] + 1)
            idx -= 1
        return
    def to_the_right(self, deriv, candies, idx):
        candies[idx] = 1
        idx += 1
        while idx < len(deriv) and deriv[idx] == 1:
            candies[idx] = candies[idx - 1] + 1
            idx += 1
        return

    def findlocalmins(self, arr):
        if len(arr) == 1:
            return [0]
        localmins = []
        if arr[1] != -1:
            localmins.append(0)
        for i in range(1, len(arr) - 1):
            if arr[i] == -1 and arr[i + 1] != -1 or arr[i] == 0 and arr[i + 1] != -1:
                localmins.append(i)
        if arr[-1] != 1:
            localmins.append(len(arr) - 1)
        return localmins
if __name__ == '__main__':
    s = Solution()
    c = s.candy([0])
    print(c)