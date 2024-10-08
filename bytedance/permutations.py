from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perm(nums):
            if len(nums) == 2:
                return [nums, nums[::-1]]
            t = nums[0]
            subperm = perm(nums[1:])
            tperm = []
            for sp in subperm:
                tperm.append([t] + sp)
                for i in range(1, len(sp) + 1):
                    tperm.append(sp[:i] + [t] + sp[i:])
            return tperm
        if len(nums) == 1:
            return [nums]
        
        res = perm(nums)
        return res
    
if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))