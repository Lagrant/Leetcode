import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        m = len(nums) - k
        for _ in range(m):
            heapq.heappop(nums)
        return heapq.heappop(nums)