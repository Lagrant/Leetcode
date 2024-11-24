from typing import List
class Solution:
    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        if len(nums) == 1:
            return

        # Create second array with 3 bucket indices
        count: list[int] = [0] * 3

        # Single pass count into buckets
        for i in range(len(nums)):
            count[nums[i]] += 1        

        # Rewrite array using bucket count
        i = 0
        for j in range(len(count)):
            while count[j] > 0:
                if i < len(nums):
                    nums[i] = j
                    count[j] -= 1
                    i += 1

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0, len(nums))

    def quicksort(self, nums, start, end):
        if end - start <= 1:
            return
        
        i, j = start + 1, end - 1
        piv = start
        while i <= j:
            if nums[i] < nums[piv]:
                nums[i], nums[piv] = nums[piv], nums[i]
                piv += 1
                i += 1
            else:
                if nums[j] < nums[piv]:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    j -= 1
        if piv > 0:
            self.quicksort(nums, start, piv)
        self.quicksort(nums, piv + 1, end)

if __name__ == '__main__':
    s = Solution()
    num = [2,0,2,1,1,0]
    s.sortColors(num)
    print(num)