class Solution:
    def threeSum(self, nums):
        sum3 = []
        dep = {}
        for i in range(len(nums)):
            piv = -nums[i]
            sum2 = {}
            for j in range(i + 1, len(nums)):
                if (nums[j] not in sum2):
                    sum2[piv - nums[j]] = j
                else:
                    cur_sum = [nums[i], nums[sum2[nums[j]]], nums[j]]
                    dep_cur = cur_sum.copy()
                    dep_cur.sort()
                    dep_str = ''.join([str(i) for i in dep_cur])
                    if (dep_str not in dep):
                        sum3.append(cur_sum)
                        dep[dep_str] = 1

        return sum3

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))