class Solution:
    def maxSubArray(self, nums):
        sub_sum = nums[0]
        sub_max = sub_sum
        for i in range(1, len(nums)):
            # if (dp_table[-1] < 0):
            #     dp_table.append(nums[i])
            #     if (sub_sum < dp_table[-1]):
            #         sub_sum = dp_table[-1]
            # else:
            #     dp_table.append(dp_table[-1] + nums[i])
            #     if (sub_sum < dp_table[-1]):
            #         sub_sum = dp_table[-1]
            if (sub_sum < 0):
                if (sub_sum < nums[i]):
                    sub_sum = nums[i]
                if (sub_max < sub_sum):
                    sub_max = sub_sum
            else:
                sub_sum += nums[i]
                if (sub_max < sub_sum):
                    sub_max = sub_sum

        return sub_max

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))