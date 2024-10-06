from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda x: x[0])
        ptr = 0
        for i in range(len(intervals) - 1):
            if intervals[i][1] < intervals[i + 1][0]:
                intervals[i + 1 - ptr] = intervals[i + 1]
                continue
            intervals[i + 1][0] = min(intervals[i][0], intervals[i + 1][0])
            intervals[i + 1][1] = max(intervals[i][1], intervals[i + 1][1])
            ptr += 1
            intervals[i + 1 - ptr] = intervals[i + 1]
        
        return intervals[:-ptr] if ptr > 0 else intervals