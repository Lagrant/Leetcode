from typing import List
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        thresh = len(nums) // 3
        n_dict = defaultdict(int)
        for n in nums:
            n_dict[n] += 1

        res = []
        for n, cnt in n_dict.items():
            if cnt > thresh:
                res.append(n)
        return res