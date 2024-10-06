from typing import List
class Solution:
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     if len(intervals) == 0:
    #         return [newInterval]
    #     if len(intervals) == 1:
    #         intervals.append(newInterval)
    #         intervals.sort(key=lambda x: x[0])
    #         if intervals[0][1] >= intervals[1][0]:
    #             intervals[0][1] = max(intervals[0][1], intervals[1][1])
    #             return [intervals[0]]
    #         else:
    #             return intervals
    #     if newInterval[0] < intervals[0][0]:
    #         if newInterval[1] < intervals[0][0]:
    #             return [newInterval] + intervals
    #         idx = self.bin_search(intervals, 1, newInterval[1])
    #         if newInterval[1] < intervals[idx + 1][0]:
    #             intervals[idx] = newInterval
    #             return intervals[idx:]
    #         else:
    #             intervals[idx + 1][0] = newInterval[0]
    #             intervals[idx + 1][1] = max(intervals[idx + 1][1], newInterval[1])
    #             return intervals[idx + 1:]
    #     elif newInterval[0] > intervals[-1][0]:
    #         if newInterval[0] <= intervals[-1][1]:
    #             intervals[-1][1] = max(intervals[-1][1], newInterval[1])
    #             return intervals
    #         else:
    #             return intervals + [newInterval]
    #     idx = self.bin_search(intervals, 0, newInterval[0])
    #     if intervals[idx][1] >= newInterval[1]:
    #         return intervals
    #     if intervals[idx][1] >= newInterval[0]:
    #         cnt = idx
    #         while cnt < len(intervals) and intervals[cnt][1] < newInterval[1]:
    #             cnt += 1
    #         if cnt < len(intervals):
    #             if intervals[cnt][0] <= newInterval[1]:
    #                 intervals[idx][1] = intervals[cnt][1]
    #                 cnt += 1
    #             else:
    #                 intervals[idx][1] = newInterval[1]
    #                 cnt = min(cnt + 1, len(intervals) - 1)
    #             return intervals[:idx + 1] + intervals[cnt:]
    #         else:
    #             intervals[idx][1] = newInterval[1]
    #             return intervals[:idx + 1]
    #     else:
    #         if newInterval[1] < intervals[idx + 1][0]:
    #             return intervals[:idx + 1] + newInterval + intervals[idx + 1:]
    #         cnt = idx + 1
    #         while cnt < len(intervals) and intervals[cnt][1] < newInterval[1]:
    #             cnt += 1
    #         if cnt < len(intervals):
    #             if intervals[cnt][0] <= newInterval[1]:
    #                 intervals[idx + 1][1] = intervals[cnt][1]
    #                 cnt += 1
    #             else:
    #                 intervals[idx + 1][1] = newInterval[1]
    #                 cnt = min(cnt + 1, len(intervals) - 1)
    #             return intervals[:idx + 2] + intervals[cnt + 1:]
    #         else:
    #             intervals[idx + 1][1] = newInterval[1]
    #             intervals[idx + 1][0] = min(intervals[idx + 1][0], newInterval[0])
    #             return intervals[:idx + 2]
            

    # def bin_search(self, arr, idx, target):
    #     i, j = 0, len(arr) - 1
    #     while abs(j - i) > 1:
    #         mid = (i + j) // 2
    #         if arr[mid][idx] < target:
    #             i = mid
    #         elif arr[mid][idx] > target:
    #             j = mid
    #         else:
    #             return mid
    #     return i
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        if len(intervals) == 1:
            intervals.append(newInterval)
            intervals.sort(key=lambda x: x[0])
            if intervals[0][1] >= intervals[1][0]:
                intervals[0][1] = max(intervals[0][1], intervals[1][1])
                return [intervals[0]]
            else:
                return intervals
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        merge = []
        startflag, getflag = False, False
        start, end = 0, len(intervals) - 1 
        for i, n in enumerate(intervals):
            if not startflag:
                if newInterval[0] <= n[0]:
                    merge.append(newInterval[0])
                    start = i
                    startflag = True
                elif newInterval[0] > n[0] and newInterval[0] <= n[1]:
                    merge.append(n[0])
                    start = i
                    startflag = True
            if startflag:
                if not getflag and newInterval[1] < n[0]:
                    merge.append(newInterval[1])
                    end = i - 1
                    break
                if newInterval[1] >= n[1]:
                    merge.append(newInterval[1])
                    end = i
                elif n[0] <= newInterval[1] and newInterval[1] < n[1]:
                    merge.append(n[1])
                    end = i
                    getflag = True
        return intervals[:start] + [[merge[0], merge[-1]]] + intervals[end + 1:]
    
    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # loop through intervals, if start of newInterval is in the middle of one interval, start = interval_start
        # else if start of newInterval is between one end and one start, start = newInterval start
        intervals.append([1e6, 1e6])
        n_start, n_end = newInterval[0], newInterval[1]
        prev_end = -1
        start, end = -1, -1
        for idx, (i_start, i_end) in enumerate(intervals):
            if prev_end < n_start <= i_start:
                start_idx = idx
                start = n_start
            elif i_start < n_start <= i_end:
                start_idx = idx
                start = i_start
            if prev_end <= n_end < i_start:
                end_idx = idx - 1
                end = n_end
                break
            elif i_start <= n_end <= i_end:
                end_idx = idx
                end = i_end
                break
            prev_end = i_end
        return intervals[:start_idx] + [[start, end]] + intervals[end_idx+1:-1]
if __name__ == '__main__':
    s = Solution()
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))