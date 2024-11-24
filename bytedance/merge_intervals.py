from typing import List
class Solution:
    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
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
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        non_overlap = []
        cur_interv = intervals[0]
        for i in range(1, len(intervals)):
            if cur_interv[0] <= intervals[i][0] <= cur_interv[1]:
                cur_interv[1] = max(cur_interv[1], intervals[i][1])
            else:
                non_overlap.append(cur_interv)
                cur_interv = intervals[i]
        non_overlap.append(cur_interv)
        return non_overlap