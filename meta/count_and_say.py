class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        i = 1
        res = '1'
        while i < n:
            res = self.rle(res)
            i += 1
        return res


    def rle(self, seq):
        if len(seq) == 1:
            return '1' + seq
        i = 0
        cnt = 0
        res  =''
        while i < len(seq) - 1:
            cnt += 1
            if seq[i] != seq[i + 1]:
                res += f'{cnt}{seq[i]}'
                cnt = 0
            i += 1
        res += f'{cnt + 1}{seq[-1]}'
        
        return res

if __name__ == '__main__':
    s = Solution()