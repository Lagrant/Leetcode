class Solution:
    def maxProfit(self, prices) -> int:
        min_pri = prices[0]
        pri_table = [-prices[0]]
        for i in range(1, len(prices)):
            pri_table.append(prices[i] - min_pri)
            if (prices[i] < min_pri):
                min_pri = prices[i]
        
        return 0 if (max(pri_table) < 0) else max(pri_table)

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))