from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        end = len(nums) - 1
        piv = end - 1
        owe_step = 0
        while piv >= 0:
            owe_step = 0 if nums[piv] + owe_step > 0 else owe_step - 1
            piv -= 1
        return not owe_step < 0


if __name__ == '__main__':
    s = Solution()
    s.canJump([0])