class Solution:
    def maxProfit(self, prices) -> int:
        for i in range(len(prices) - 1, -1, -1):
            prices[i] = prices[i] - prices[i - 1]
        cur_prof = 0
        max_prof = 0
        for i in range(1, len(prices)):
            if cur_prof + prices[i] < 0:
                max_prof = max(max_prof, 0, cur_prof)
                cur_prof = 0
            else:
                cur_prof += prices[i]
                max_prof = max(max_prof, cur_prof)
        max_prof = max(max_prof, 0, cur_prof)
        return max_prof
    
if __name__ == '__main__':
    s = Solution()
    k = s.maxProfit([7,1,5,3,6,4])
    print(k)