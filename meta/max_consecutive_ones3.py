from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0] if k == 0 else 1
        start, end = 0, 0
        quota = k
        maxones = 0
        while end < len(nums):
            if nums[end] == 0:
                if quota > 0:
                    quota -= 1
                    end += 1
                    maxones = max(maxones, end - start)
                else:
                    if nums[start] == 0:
                        end += 1
                        start += 1
                    else:
                        start += 1
            else:
                maxones = max(maxones, end - start + 1)
                end += 1
        return maxones
    
class Solution1:
    def longestOnes(self, A: List[int], K: int) -> int:
      left = right = 0
      
      for right in range(len(A)):
        # if we encounter a 0 the we decrement K
        if A[right] == 0:
          K -= 1
        # else no impact to K
        
        # if K < 0 then we need to move the left part of the window forward
        # to try and remove the extra 0's
        if K < 0:
          # if the left one was zero then we adjust K
          if A[left] == 0:
            K += 1
          # regardless of whether we had a 1 or a 0 we can move left side by 1
          # if we keep seeing 1's the window still keeps moving as-is
          left += 1
      
      return right - left + 1