class Solution:
    """
    This idea is similar to water container that I should sort 
    get more information. Then find values starting from both sides, 
    if it is bigger than 0, the right side move one step to the left 
    and vice versa.
    """
    def threeSum(self, nums):
        sum3 = []
        nums.sort()
        for i, n in enumerate(nums):
            if (i > 0 and n == nums[i-1]):
                continue
            cur = -n
            l = i + 1
            r = len(nums) - 1
            while (l < r):
                if (nums[l] + nums[r] == cur):
                    sum3.append([n, nums[l], nums[r]])
                    l += 1
                    while (l < r and nums[l] == nums[l-1]):
                        l += 1
                    r -= 1
                    while (l < r and nums[r] == nums[r+1]):
                        r -= 1
                elif (nums[l] + nums[r] < cur):
                    l += 1
                else:
                    r -= 1
        return sum3

sol = Solution()
print(sol.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))