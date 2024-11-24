from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.cum_sum = [0]*(len(nums)+1)
        cum_sum = 0
        for i in range(1,len(nums)+1):
            cum_sum += nums[i-1]
            self.cum_sum[i] = cum_sum

    def sumRange(self, left: int, right: int) -> int:
        result = self.cum_sum[right+1] - self.cum_sum[left]
        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)