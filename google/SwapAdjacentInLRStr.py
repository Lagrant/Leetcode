from collections import deque
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """
        XL -> LX
        RX -> XR
        """
        lr_start = start.replace('X', '')
        lr_end = end.replace('X', '')
        if (lr_end != lr_start):
            return False

        start_r = deque([])
        start_l = deque([])
        for i in range(len(start)):
            if (start[i] == end[i]):
                 continue
            
            if (start[i] == 'X' and end[i] == 'R'):
                if (len(start_r) == 0):
                    return False
                else:
                    start_r.pop()
            elif (start[i] == 'L' and end[i] == 'X'):
                if (len(start_l) == 0):
                    return False
                else:
                    start_l.pop()

            elif (start[i] == 'R' and end[i] == 'X'): # in this case, end[i] must be X
                start_r.append('R')
            elif (start[i] == 'X' and end[i] == 'L'):
                start_l.append('X')

        if (len(start_r) > 0 or len(start_l) > 0):
            return False
        return True

sol = Solution()
print(sol.canTransform("XLXRRXXRXX", "LXXXXXXRRR"))