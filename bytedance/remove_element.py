from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        head = 0
        tail = len(nums) - 1
        if head == tail and nums[head] != val:
            return 1
        while head <= tail:
            if nums[head] != val:
                head += 1
            else:
                while nums[tail] == val and head <= tail:
                    tail -= 1
                if head <= tail:
                    nums[head], nums[tail] = nums[tail], nums[head]
        return head
    
    def removeElement1(self, nums: List[int], val: int) -> int:
        k=0
        n = len(nums)
        for i in range(n):
            if nums[i] == val:
                k+=1
            else:
                nums[i-k]=nums[i]
        return n-k

if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3,2,2,3], 3))