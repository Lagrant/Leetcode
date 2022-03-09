class Solution:
    def insert(self, intervals, newInterval):
        if (len(newInterval) == 0):
            return intervals
        if (len(intervals) == 0):
            return [newInterval]
        if (newInterval[0] > intervals[-1][1]):
            intervals.append(newInterval)
            return intervals
        if (newInterval[1] < intervals[0][0]):
            newInterval = [newInterval]
            newInterval.extend(intervals)
            return newInterval
        
        if (newInterval[0] > intervals[-1][0]):
            pos = len(intervals) - 1
        else:
            pos = -1
            start, end = 0, len(intervals) - 1
            val = newInterval[0]
            while (end - start > 1):
                mid = int((start + end) / 2)
                if (val < intervals[mid][0]):
                    end = mid
                elif (val > intervals[mid][0]):
                    start = mid
                else:
                    pos = mid
                    break
            pos = start if (pos == -1) else mid
        
        if (pos == 0 and newInterval[0] < intervals[0][0]):
            intervals[0][0] = newInterval[0]

        elif (pos == len(intervals) - 1 and newInterval[0]> intervals[-1][0]):
            newInterval[0] = intervals[-1][0]

        covered = False
        if (intervals[pos][1] >= newInterval[0]):
            covered = True
        if (intervals[pos][1] < newInterval[0]):
            pos += 1
            if (pos != len(intervals) and intervals[pos][0] <= newInterval[1]):
                intervals[pos][0] = newInterval[0]
                covered = True

        end = pos
        for i in range(pos, len(intervals)):
            if (covered):
                if (newInterval[1] < intervals[i][0]):
                    end = i - 1
                    intervals[pos][1] = newInterval[1]
                    break
                if (newInterval[1] <= intervals[i][1]):
                    end = i
                    intervals[pos][1] = intervals[end][1]
                    break
                if (newInterval[1] > intervals[i][1]):
                    intervals[pos][1] = newInterval[1]
                    end = i
            else:
                if (newInterval[1] < intervals[i][0]):
                    # end = i
                    temp = intervals[i:]
                    intervals = intervals[:i]
                    intervals.append(newInterval)
                    intervals.extend(temp)
                    break
                if (newInterval[1] <= intervals[i][1]):
                    end = i
                    intervals[pos][1] = intervals[end][1]
                    break
                if (newInterval[1] > intervals[i][1]):
                    intervals[pos][1] = newInterval[1]
                    end = i

        rmv_len = end - pos
        for i in range(end + 1, len(intervals)):
            intervals[i - rmv_len] = intervals[i]
        intervals = intervals[:len(intervals) - rmv_len]
        return intervals

sol = Solution()
print(sol.insert(intervals = [[3,6],[9,9],[11,13],[14,14],[16,19],[20,22],[23,25],[30,34],[41,43],[45,49]], newInterval = [29, 32]))

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Similar to merge intervals, here intervals are already sorted
        """
        res = []
        
        for i, interval in enumerate(intervals):
            
            # if new interval is next, insert current
            if newInterval[0]> interval[1]:
                res.append(interval)
             
            #interval is after newinterval
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                
                return res + intervals[i:]
            
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
                
                
        res.append(newInterval)
        
        return res