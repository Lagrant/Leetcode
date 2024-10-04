from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 2
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i + 2], nums[j] = nums[j], nums[i + 2]
                i += 1
                j += 1
            else:
                j += 1
        return i + 2