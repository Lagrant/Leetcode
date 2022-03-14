class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if (amount == 0):
            return 0
        
        cnt_lst = [-1] * (amount + 1)
        cnt_lst[0] = 0
        for i in range(amount + 1):
            temp = []
            for c in coins:
                if (i - c >= 0 and cnt_lst[i - c] != -1):
                    temp.append(cnt_lst[i - c] + 1)
            if (any(temp)):
                cnt_lst[i] = min(temp)
        
        return cnt_lst[-1]

sol = Solution()
print(sol.coinChange([5, 3], 7))