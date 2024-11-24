from typing import List
import functools
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        y_end = -float('inf')
        ans = 0
        for x, y in intervals:
            if y_end <= x:
                y_end = y
            else:
                ans += 1
        return ans


