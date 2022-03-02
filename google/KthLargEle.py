class Heap:
    def __init__(self, capacity) -> None:
        self.heap = [] * (capacity + 1)
        self.size = 0
        self.capacity = capacity
    
    def parent(self, i):
        return int(i - 1) / 2
    
    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, k):
        self.heap[self.size] = k
        i = self.size
        self.size += 1
        while (i > 0):
            p = self.parent(i)
            if (self.heap[p] < k):
                self.swap(p, i)
            else:
                break
            i = p
        if (self.size >= self.capacity):
            self.size = self.capacity - 1

class Solution1:
    """
    The min heap can filter out the first k largest elements
    """
    def findKthLargest(self, nums, k: int) -> int:
        max_h = Heap(k)

        for n in nums:
            max_h.insert(n)

import heapq

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap) # this is a min heap
        
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
                
        return heapq.heappop(heap)

sol = Solution()
print(sol.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))