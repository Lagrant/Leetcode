from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        table = [nums[0], nums[1]]
        for i in range(2, len(nums)):
            locmax = max(table[:i - 1]) + nums[i]
            table.append(locmax)
        return max(table)