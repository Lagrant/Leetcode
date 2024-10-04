from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums) - 1

        piv = 0
        jump = 1
        s_size = nums[piv]
        if s_size >= len(nums) - 1:
            return 1

        while piv < len(nums):
            max_step = 0
            jump += 1
            for i in range(piv + 1, piv + s_size + 1):
                max_step = i + nums[i] if i + nums[i] > max_step else max_step
                if max_step >= len(nums) - 1:
                    return jump
            piv += nums[piv]
            s_size = max_step - piv
        return jump

if __name__ == '__main__':
    s = Solution()
    print(s.jump([2,3,0,1,4]))    