from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        sarr, i, start, end = [], 1, 0, 0
        while i < len(nums):
            if nums[i] == nums[i - 1] + 1:
                end = i
            else:
                sarr.append(f'{nums[start]}->{nums[end]}' if end > start else f'{nums[start]}')
                end = start = i
            i += 1
        sarr.append(f'{nums[start]}->{nums[end]}' if end > start else f'{nums[start]}')
        return sarr