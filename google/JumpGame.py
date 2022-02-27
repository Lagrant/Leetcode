class Solution:
    def canJump(self, nums) -> bool:
        if (len(nums) == 0):
            return False
        max_reach = nums[0]
        pos = 0
        while (pos < len(nums) and pos <= max_reach):
            if (pos == len(nums) - 1):
                return True
            if (nums[pos] + pos > max_reach):
                max_reach = nums[pos] + pos
                if (max_reach >= len(nums) - 1):
                    return True
            pos += 1
        
        return False

sol = Solution()
print(sol.canJump([]))