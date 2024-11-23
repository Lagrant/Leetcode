from typing import List
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 != 0 or target > total or target < -total:
            return 0
        sums = defaultdict(int)
        sums[nums[0]] += 1
        sums[-nums[0]] += 1
        for i in range(1, len(nums)):
            s_temp = defaultdict(int)
            for n in sums:
                s_temp[n + nums[i]] += sums[n]
                s_temp[n - nums[i]] += sums[n]
            sums = s_temp
        return sums[target]