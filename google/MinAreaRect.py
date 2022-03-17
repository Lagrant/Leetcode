import math
from collections import defaultdict
class Solution:
    def match(self, col1, col2):
        y = -1
        min_h = float('inf')
        i, j = 0, 0
        while (i < len(col1) and j < len(col2)):
            if (col1[i] > col2[j]):
                j += 1
            elif (col1[i] < col2[j]):
                i += 1
            else:
                if (y == -1):
                    y = col2[j]
                    i += 1
                    j += 1
                else:
                    min_h = col2[j] - y if (col2[j] - y < min_h) else min_h
                    y = col2[j]
                    i += 1
                    j += 1
        return min_h

    def minAreaRect(self, points) -> int:
        cols = defaultdict(list)
        rows = defaultdict(list)
        for point in points:
            cols[point[0]].append(point[1])
            rows[point[1]].append(point[0])
        for y in cols:
            cols[y].sort()
        for x in rows:
            rows[x].sort()
        
        min_area = float('inf')
        x_coors = list(cols.keys())
        for i in range(len(x_coors)):
            if (len(cols[x_coors[i]]) == 1):
                continue
            for j in range(i+1, len(x_coors)):
                if (len(cols[x_coors[j]]) == 1):
                    continue
                min_h = self.match(cols[x_coors[i]], cols[x_coors[j]])
                if (math.isinf(min_h)):
                    continue
                area = min_h * abs(x_coors[i] - x_coors[j])
                min_area = area if (area < min_area) else min_area
        if (math.isinf(min_area)):
            return 0
        return min_area

sol = Solution()
print(sol.minAreaRect([[0,1],[0,0],[3,4],[2,1],[1,3],[2,3],[1,0],[4,1],[0,2]]))