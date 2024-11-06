from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = end = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                start = end = i
                break
            i += 1
        
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
            end += 1
            i += 1
        