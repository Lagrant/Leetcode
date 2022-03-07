class Solution:
    def __init__(self) -> None:
        self.even = ['11', '69', '88', '96', '00']
        self.odd = ['0', '1', '8']
        self.sb_lst = []

    def findStrobogrammatic(self, n: int):

        if (n == 1):
            return self.odd
        elif (n == 2):
            return self.even[:-1]
        
        if (n % 2 == 0):
            for e in self.even:
                self.sub_sb(e, n - 2) 
        if (n % 2 == 1):
            for o in self.odd:
                self.sub_sb(o, n - 1)         
        return self.sb_lst
        
    def sub_sb(self, e, k):
        if (k == 0 and e[0] != '0'):
            self.sb_lst.append(e)
            return
        elif (k == 0 and e[0] == '0'):
            return
            
        for c in self.even:
            self.sub_sb(c[0] + e + c[1], k - 2)

sol = Solution()
print(sol.findStrobogrammatic(3))