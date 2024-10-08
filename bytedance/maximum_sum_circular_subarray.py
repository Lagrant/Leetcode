from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsofar, maxtoend = -float('inf'), -float('inf')
        minsofar, mintoend = float('inf'), float('inf')
        for n in nums:
            maxtoend = max(n, maxtoend + n)
            maxsofar = max(maxtoend, maxsofar)

            mintoend = min(n, mintoend + n)
            minsofar = min(mintoend, minsofar)
        
        if maxsofar < 0:
            return maxsofar
        else:
            return max(sum(nums) - minsofar, maxsofar)

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubarraySumCircular([5, -3, 5]))