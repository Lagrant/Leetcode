class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        seg_size = 2 * numRows - 2
        cols = len(s) // seg_size
        res = len(s) % seg_size
        cols = cols + 1 if res > 0 else cols
        s1 = ''
        
        for i in range(cols):
            s1 += s[i * seg_size]
        for j in range(1, numRows - 1):
            for i in range(cols):
                if i * seg_size + j < len(s):
                    s1 += s[i * seg_size + j]
                else:
                    break
                if i * seg_size + seg_size - j < len(s):
                    s1 += s[i * seg_size + seg_size - j]
                else:
                    break
        for i in range(cols):
            if i * seg_size + numRows - 1 < len(s):
                s1 += s[i * seg_size + numRows - 1]

        return s1
