from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        piv, i, j = 0, 0, 0
        while i < k and j < len(arr):
            piv += 1
            if piv != arr[j]:
                i += 1
            else:
                j += 1
        
        if i < k:
            piv += k - i
        return piv