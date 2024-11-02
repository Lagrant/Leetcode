from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] >= target else 1
        i, j = 0, len(nums)
        while abs(i - j) != 1:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                j = mid
            else:
                i = mid
        if i == j:
            return i
        i, j = min(i, j), max(i, j)
        if target <= nums[i]:
            return i
        return j