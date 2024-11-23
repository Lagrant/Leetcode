from typing import List
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.idx = {}
        for i, n in enumerate(nums):
            if n in self.idx:
                self.idx[n].append(i)
            else:
                self.idx[n] = [i]

    def pick(self, target: int) -> int:
        if target in self.idx:
            return self.idx[target][random.randint(0, len(self.idx[target]) - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)