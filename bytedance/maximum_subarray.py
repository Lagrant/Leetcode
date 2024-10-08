class Solution:
    def maxSubArray(self, nums):
        maxsofar = -float('inf')
        maxtoend = -float('inf')
        for n in nums:
            maxtoend = max(n, n + maxtoend)
            maxsofar = max(maxsofar, maxtoend)
        return maxsofar