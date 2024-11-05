from typing import List
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        topb = 0
        hlist = []
        for i in range(len(heights) - 1, -1, -1):
            if topb < heights[i]:
                hlist.append(i)
                topb = heights[i]
        return sorted(hlist)