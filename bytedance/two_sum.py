from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2 and sum(nums) == target:
            return [0, 1]
        n_dict = {}
        for i, n in enumerate(nums):
            if target - n not in n_dict:
                n_dict[n] = i
            else:
                return [i, n_dict[target - n]]