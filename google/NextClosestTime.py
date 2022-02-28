class Solution:
    def nextClosestTime(self, time: str) -> str:
        dig_str = time.replace(':', '')
        digs = [int(s) for s in dig_str]
        s_digs = digs.copy()
        s_digs.sort()

        for d in s_digs:
            if (d > digs[-1]):
                digs[-1] = d
                return str(digs[0]) + str(digs[1]) + ':' + str(digs[2]) + str(digs[3])
        
        for d in s_digs:
            if (d < 6):
                if (d > digs[2]):
                    digs[2] = d
                    digs[-1] = s_digs[0]
                    return str(digs[0]) + str(digs[1]) + ':' + str(digs[2]) + str(digs[3])
            else:
                break
        
        max_h = 10 if (digs[0] < 2) else 4
        for d in s_digs:
            if (d < max_h):
                if (d > digs[1]):
                    digs[1] = d
                    digs[2] = digs[3] = s_digs[0]
                    return str(digs[0]) + str(digs[1]) + ':' + str(digs[2]) + str(digs[3])
            else:
                break
        
        for d in s_digs:
            if (d < 3):
                if (d > digs[0]):
                    digs[0] = d
                    digs[1] = digs[2] = digs[3] = s_digs[0]
                    return str(digs[0]) + str(digs[1]) + ':' + str(digs[2]) + str(digs[3])
            else:
                break
        
        digs[0] = digs[1] = digs[2] = digs[3] = s_digs[0]
        return str(digs[0]) + str(digs[1]) + ':' + str(digs[2]) + str(digs[3])

sol = Solution()
print(sol.nextClosestTime("18:42"))