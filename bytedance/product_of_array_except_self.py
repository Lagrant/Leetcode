from typing import List

class Solution:
    def __init__(self) -> None:
        self.outputs = None
        self.nums = None
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # zeros = 0
        # for n in nums:
        #     zeros = zeros + 1 if n == 0 else zeros
        # if zeros > 1:
        #     return [0] * len(nums)
        if len(nums) == 2:
            return [nums[1], nums[0]]
        elif len(nums) == 3:
            return[nums[1] * nums[2], nums[0] * nums[2], nums[1] * nums[0]]
        self.nums = nums
        self.outputs = [None] * len(nums)
        intermediate_res = []
        n_size = len(nums)
        half_nums = nums
        while n_size > 3:
            odd = n_size % 2 == 1
            n_size = n_size - 1 if odd else n_size
            interm_r = []
            for i in range(0, n_size, 2):
                interm_r.append(half_nums[i] * half_nums[i + 1])
            if odd:
                interm_r[-1] *= half_nums[-1]
            half_nums = interm_r
            intermediate_res.append(interm_r)
            n_size //= 2
        
        
        self.cummulative(intermediate_res, 1, 0)
        print(intermediate_res)
        print(self.outputs)
        return self.outputs

    def cummulative(self, arr, cum, idx):
        if len(arr) == 0:
            if len(self.nums) % 2 == 1 and idx * 2 + 2 == len(self.nums) - 1:
                self.outputs[idx * 2] = cum * self.nums[idx * 2 + 1] * self.nums[idx * 2 + 2]
                self.outputs[idx * 2 + 1] = cum * self.nums[idx * 2] * self.nums[idx * 2 + 2]
                self.outputs[idx * 2 + 2] = cum * self.nums[idx * 2] * self.nums[idx * 2 + 1]
            else:
                self.outputs[idx * 2] = cum * self.nums[idx * 2 + 1]
                self.outputs[idx * 2 + 1] = cum * self.nums[idx * 2]
            return
        
        if len(arr[-1]) % 2 == 1 and idx * 2 + 2 == len(arr[-1]) - 1:
            self.cummulative(arr[:-1], cum * arr[-1][idx * 2] * arr[-1][idx * 2 + 1], idx * 2 + 2)
            self.cummulative(arr[:-1], cum * arr[-1][idx * 2] * arr[-1][idx * 2 + 2], idx * 2 + 1)
            self.cummulative(arr[:-1], cum * arr[-1][idx * 2 + 2] * arr[-1][idx * 2 + 1], idx * 2)
        else:
            self.cummulative(arr[:-1], cum * arr[-1][idx * 2], idx * 2 + 1)
            self.cummulative(arr[:-1], cum * arr[-1][idx * 2 + 1], idx * 2)

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        print(res)
        postfix = 1
        for i in range(len(nums) - 2, -1, -1):
            postfix *= nums[i+1]
            res[i] *= postfix
        return res

if __name__ == '__main__':
    s = Solution()
    s.productExceptSelf([2,4,-2,1,2,-1,4,1,3,-3,-1,2,1,2,1,-3,1,-1,1,3,3,-2,-2,3,-3,-1,1,-2,-4,-2])
