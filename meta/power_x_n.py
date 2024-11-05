class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = 1 if n > 0 else -1
        n = sign * n
        bin_n = bin(n)[2:]
        rec = []
        cum = x
        for b in bin_n[::-1]:
            if b == '1':
                rec.append(cum)
            cum *= cum
        res = 1
        for r in rec:
            res *= r
        if sign == -1:
            res = 1 / float(res)
        return res
