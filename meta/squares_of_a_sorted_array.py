from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [n ** 2 for n in nums]
        return sorted(nums)