from typing import List
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            if (nums[i] < nums[i+1]):
                for j in range(len(nums) - 1, i, -1):
                    if (nums[j] > nums[i]):
                        nums[j], nums[i] = nums[i], nums[j]
                        nums[i+1:] = sorted(nums[i+1:])
                        break
                break
            elif (i == 0):
                nums.sort()
    
    def nextPermutation1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1 :] = sorted(nums[i + 1 :])

if __name__ == '__main__':
    s = Solution()
    num = [1,2,3,4,6,5]
    s.nextPermutation(num)
    print(num)