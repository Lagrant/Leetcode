from typing import List
from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        cum = [nums[0] % k]
        for i in range(1, len(nums)):
            cum.append((cum[-1] + nums[i]) % k)
            if cum[-1] == 0:
                return True
        k_dict = defaultdict(list)
        for i, c in enumerate(cum):
            if c not in k_dict:
                k_dict[c] = [1, [i]]
            else:
                if k_dict[c][0] == 1 and k_dict[c][1][0] == i - 1:
                    k_dict[c][1].append(i)
                    k_dict[c][0] += 1
                else:
                    return True
        return False
    
    def checkSubarraySum1(self, nums: List[int], k: int) -> bool:
        comps = {0:-1}
        cusum = 0
        for i, n in enumerate(nums):
            cusum+=n
            rem = cusum%k
            if rem in comps:
                if i - comps[rem]>1:
                    return True
            else:
                comps[rem] = i
        
        return False
    
if __name__ == '__main__':
    s = Solution()
    print(s.checkSubarraySum([1,0], 2))