from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return -1 if nums[0] != target else 0
        
        if len(nums) == 2:
            return -1 if target not in nums else nums.index(target)
        
        i, j = 0, len(nums) - 1
        mid = (i + j) // 2
        while abs(i - j) > 1:
            if nums[mid] == target:
                return mid
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            
            if nums[mid] > nums[i]:
                if nums[mid] > target > nums[i]:
                    j = mid
                else:
                    i = mid
            else:
                if nums[mid] < target < nums[j]:
                    i = mid
                else:
                    j = mid
            mid = (i + j) // 2
            
        return -1