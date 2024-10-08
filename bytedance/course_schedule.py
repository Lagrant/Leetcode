from typing import List
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1:
            return True
        
        pre = defaultdict(list)
        post = defaultdict(dict)
        for (i, j) in prerequisites:
            pre[j].append(i)
            post[i][j] = True
        starts = []
        for i in range(numCourses):
            if i not in post:
                starts.append(i)
        if len(starts) == 0:
            return False
        
        while len(starts) > 0:
            s = starts.pop()
            if s not in pre:
                continue
            c_lst = pre[s]
            del pre[s]
            for c in c_lst:
                del post[c][s]
                if len(post[c]) == 0:
                    del post[c]
                    starts.append(c)
                if len(post) == 0:
                    return True
        return not len(post) > 0