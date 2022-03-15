class Solution:
    def comp_L(self, start, end):
        if (start == 'XL' and end == 'LX' or\
            start == end == 'LX' or\
            start == end == 'XL'):
            return 2
        if (start[0] == end[0] == 'L'):
            return 1
        else:
            return -1
    def comp_R(self, start, end):
        if (start == 'RX' and end == 'XR' or\
            start == end == 'RX' or\
            start == end == 'XR'):
            return 2
        if (start[0] == end[0] == 'R'):
            return 1
        else:
            return -1
    def comp_X(self, start, end):
        if (start == end =='XX'):
            return 1
        else:
            return -1
    def canTransform(self, start: str, end: str) -> bool:
        """
        XL -> LX
        RX -> XR

        RXXXXXL
        LXXXXXR
        RXR
        LLX
        LXL
        """
        lr_start = start.replace('X', '')
        lr_end = end.replace('X', '')
        if (lr_end != lr_start):
            return False

        i = 0
        while (i < len(start) - 1):
            move_X = self.comp_X(start[i:i+2], end[i:i+2])
            if (move_X != -1):
                i += move_X
                continue
            
            move_L = self.comp_L(start[i:i+2], end[i:i+2])
            if (move_L != -1):
                i += move_L
                continue

            move_R = self.comp_R(start[i:i+2], end[i:i+2])
            if (move_R != -1):
                i += move_R
                continue
            
            return False
        if (i == len(start) - 1):
            if(start[i] == end[i]):
                return True
            else:
                return False
        return True

sol = Solution()
print(sol.canTransform("XXXLXXX","XXXLXXX"))