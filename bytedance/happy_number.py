class Solution:
    def isHappy(self, n: int) -> bool:
        rec = {}
        
        while n not in rec and n != 1:
            rec[n] = 1
            n = sum(map(lambda x: int(x) ** 2, list(str(n))))
            if n == 1:
                return True
            
        return n == 1
    
if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))