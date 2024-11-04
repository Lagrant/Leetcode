from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        m, n = len(firstList), len(secondList)
        if m == 0 or n == 0:
            return []
        rt = []
        while i < m and j < n:
            interv, movement = self.findintersection(firstList[i], secondList[j])
            if len(interv) > 0:
                rt.append(interv)
            if movement == 2:
                j += 1
            elif movement == 1:
                i += 1
            else:
                i += 1
                j += 1
        return rt
    def findintersection(self, interv1, interv2):
        if interv1[0] > interv2[1] or interv1[1] < interv2[0]:
            return [], 1 if interv1[1] < interv2[1] else 2
        inters = [max(interv2[0], interv1[0]), min(interv1[1], interv2[1])]
        if interv2[1] < interv1[1]:
            n = 2
        elif interv1[1] < interv2[1]:
            n = 1
        else:
            n = 3
        return inters, n
        
