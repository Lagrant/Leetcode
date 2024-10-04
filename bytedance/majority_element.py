from typing import List
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        voting = defaultdict(int)
        threshold = len(nums) // 2 + 1
        for n in nums:
            voting[n] += 1
            if voting[n] >= threshold:
                return n
    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]