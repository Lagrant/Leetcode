from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        i, j = 0, len(nums) - 1
        mid = (i + j) // 2
        if nums[mid] > min(nums[i], nums[j]) and nums[mid] < max(nums[i], nums[j]):

    def search_subarray(self, nums):