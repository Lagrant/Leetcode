class Solution:
    def maxDistToClosest(self, seats) -> int:
        l, r, longest0 = 0, 0, 0
        seat_len = len(seats)
        left0 = -1
        while (r < seat_len):
            if (seats[r] == 1):
                cur_len = r - l
                if (left0 == -1):
                    left0 = cur_len
                if (cur_len > longest0):
                    longest0 = cur_len
                r += 1
                l = r
            else:
                r += 1
        if (l == r):
            right0 = 0
        else:
            right0 = r - l
        
        return max(left0, right0, int((longest0 + 1) / 2))

sol = Solution()
print(sol.maxDistToClosest([0,1]))