from typing import List
from collections import defaultdict
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        cum = nums[0]
        c_dict = defaultdict(list)
        c_dict[nums[0]].append(1)
        for i in range(1, len(nums)):
            cum += nums[i]
            if len(c_dict[cum]) < 2:
                c_dict[cum].append(i + 1)
            else:
                c_dict[cum][1] = i + 1
        
        max_l = 0
        for d, ls in c_dict.items():
            if d == k:
                max_l = max(max_l, ls[1] if len(ls) == 2 else ls[0])
            if d - k in c_dict:
                minidx = c_dict[d - k][0]
                maxidx = ls[1] if len(ls) == 2 else ls[0]
                max_l = max(max_l, maxidx - minidx)
        return max_l

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArrayLen([-2,-1,2,1], 1))