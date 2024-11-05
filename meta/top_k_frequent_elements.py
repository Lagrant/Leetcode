from typing import List
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for n in nums:
            if n not in freq_dict:
                freq_dict[n] = [n, 0]
            else:
                freq_dict[n][1] += 1
        freq_cnt = list(freq_dict.values())
        freq_cnt.sort(key=lambda x: x[1])
        freq_cnt = freq_cnt[-k:]
        return [f[0] for f in freq_cnt]
    
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        min_heap = []
        result = []

        for num, freq in count.items():
            if len(min_heap) == k:
                heapq.heappushpop(min_heap, (freq, num))
            else:
                heapq.heappush(min_heap, (freq, num))
        
        for _ in range(k):
            _, num = heapq.heappop(min_heap)
            result.append(num)
        
        return result