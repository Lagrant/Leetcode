from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, max_cap = 0, len(height) - 1, 0
        while i < j:
            cur_cap = (j - i) * min(height[i], height[j])
            if cur_cap > max_cap:
                max_cap = cur_cap
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_cap