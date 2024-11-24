from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        up_to_date = [0] * days[-1]
        days = [d - 1 for d in days]
        for i in range(days[-1] + 1):
            if i not in days:
                if i == 0:
                    up_to_date[i] = 0
                else:
                    up_to_date[i] = up_to_date[i-1]
                continue
            cost1 = up_to_date[max(0, i - 1)] + costs[0]
            if i - 7 < 0:
                cost2 = costs[1]
            else:
                cost2 = up_to_date[i - 7] + costs[1]
            if i - 30 < 0:
                cost3 = costs[2]
            else:
                cost3 = up_to_date[i - 30] + costs[2]
            up_to_date[i] = min((cost1, cost2, cost3))
        return up_to_date[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.mincostTickets([1,4,6,7,8,20], [2,7,15]))