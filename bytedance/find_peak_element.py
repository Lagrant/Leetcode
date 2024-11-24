from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return nums.index(max(nums))
        i, j = 0, len(nums) - 1
        mid = (i + j) // 2
        if max([nums[i], nums[j], nums[mid]]) == nums[i]:
            return i + self.findPeakElement(nums[i: mid])
        elif max([nums[i], nums[j], nums[mid]]) == nums[j]:
            return mid + 1 + self.findPeakElement(nums[mid + 1:])
        else:
           p1 = self.findPeakElement(nums[:mid + 1])
           p2 = self.findPeakElement(nums[mid:])
           if p2 == 0 and p1 == mid:
               return mid
           if p1 == mid:
               return mid + p2
           else:
               return p1
        
        
if __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement([1,2,3,4,5,6,1]))