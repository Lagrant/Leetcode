from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for i in range(len(prices) - 1, -1, -1):
            prices[i] = prices[i] - prices[i - 1]
        prof = 0
        for i in range(1, len(prices)):
            if prices[i] > 0:
                prof += prices[i]
        return prof
    
if __name__ == '__main__':
    s = Solution()
    t = s.maxProfit([7,6,4,3,1])
    print(t)