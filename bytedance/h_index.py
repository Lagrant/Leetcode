from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        h_index = 0
        for i in range(len(citations)):
            h_index = max(min(citations[i], len(citations) - i), h_index)
        return h_index
    
if __name__ == '__main__':
    s = Solution()
    print(s.hIndex([3,0,6,1,5]))