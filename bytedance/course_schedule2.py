from typing import List
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]
        
        pre = defaultdict(list)
        post = defaultdict(dict)
        for (i, j) in prerequisites:
            pre[j].append(i)
            post[i][j] = True
        starts = []
        ans = []
        ans_ = {}
        for i in range(numCourses):
            if i not in post:
                starts.append(i)
                ans_[i] = 1
                ans.append(i)
        if len(starts) == 0:
            return []
        
        
        while len(starts) > 0:
            s = starts.pop()
            if s not in ans_:
                ans.append(s)
                ans_[s] = 1
            if s not in pre:
                continue
            c_lst = pre[s]
            del pre[s]
            for c in c_lst:
                del post[c][s]
                if len(post[c]) == 0:
                    del post[c]
                    starts.append(c)
                    if c not in ans_:
                        ans.append(c)
                        ans_[c] = 1
                if len(post) == 0:
                    # for s in starts:
                    #     if s not in ans_:
                    #         ans.append(s)
                    #         ans_[s] = 1
                    return ans

        return [] if len(post) > 0 else ans
    
if __name__ == '__main__':
    s = Solution()
    print(s.findOrder(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]))