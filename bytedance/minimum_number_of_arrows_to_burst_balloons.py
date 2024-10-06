from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points.sort(key=lambda x: x[0])
        cnt = 0
        inters = []
        for (s, e) in points:
            if len(inters) == 0 or inters[1] < s:
                cnt += 1
                inters = [s, e]
                continue
            if inters[0] <= s <= inters[1] <= e:
                inters = [s, inters[1]]
            elif s <= inters[0] <= e <= inters[1]:
                inters = [inters[0], e]
            elif inters[0] <= s and inters[1] >= e:
                inters = [s, e]
        return cnt
