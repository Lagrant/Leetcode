from typing import List
import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.rng = list(range(len(w)))
        sw = sum(w)
        self.prob = [i / sw for i in w]
        self.cum_prob = [self.prob[0]]
        for i in range(1, len(self.prob) - 1):
            self.cum_prob.append(self.cum_prob[-1] + self.prob[i])

    def pickIndex(self) -> int:
        if len(self.w) == 1:
            return 0
        rd = random.random()
        idx = self.bi_search(rd)
        return self.rng[idx]

    def bi_search(self, d):
        i, j = 0, len(self.cum_prob) - 1
        while abs(j - i) > 1:
            mid = (i + j) // 2
            if self.cum_prob[mid] > d:
                if mid == 0 or self.cum_prob[mid - 1] <= d:
                    return mid
                j = mid
            elif self.cum_prob[mid + 1] > d:
                return mid + 1
            else:
                i = mid
            mid = (i + j) // 2

        if self.cum_prob[i] > d:
            return i
        elif self.cum_prob[j] <= d:
            return j + 1
        else:
            return j
            

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()