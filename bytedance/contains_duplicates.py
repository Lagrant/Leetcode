from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n_dict = {}
        for i, n in enumerate(nums):
            if n in n_dict and abs(i - n_dict[n]) <= k:
                return True
            else:
                n_dict[n] = i
        return False