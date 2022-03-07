class DSU:
    def __init__(self,N):
        self.cnt = 0
        # self.parent=list(range(N))
        self.parent = {}
    def union(self,x,y):
        a = self.findPar(x)
        b = self.findPar(y)
        if (a != b):
            self.cnt -= 1
            self.parent[self.findPar(a)]=self.findPar(b)
    def findPar(self,x):
        if (x not in self.parent):
            self.cnt += 1
            self.parent[x] = x

        if self.parent[x]!=x:
            self.parent[x]=self.findPar(self.parent[x])
        return self.parent[x]
class Solution:
    def removeStones(self, stones) -> int:
        N=len(stones)
        uf=DSU(N)
        for i in range(N):
            x = stones[i][0] + 1
            y = - stones[i][1] - 1
            uf.union(x, y)

        return N - uf.cnt

sol = Solution()
print(sol.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))