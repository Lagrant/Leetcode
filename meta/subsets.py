from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        sset = self.subsets(nums[1:])
        sset1 = []
        for s in sset:
            sset1.append(s + [nums[0]])
            sset1.append(s)
        return sset1