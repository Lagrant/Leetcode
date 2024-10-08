from typing import List
class Solution:
    # def __init__(self) -> None:
        # self.visited = {}
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    self.search_neigh(grid, [i, j])
        return cnt
    def search_neigh(self, grid, cur):
        q = [cur]
        while len(q) > 0:
            c = q.pop()
            if grid[c[0]][c[1]] == '0':
                continue

            # self.visited[cstr] = True
            grid[c[0]][c[1]] = '0'
            direc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for d in direc:
                n_cur = [d[0] + c[0], d[1] + c[1]]
                if 0 <= n_cur[0] < len(grid) and 0 <= n_cur[1] < len(grid[0]):
                    if grid[n_cur[0]][n_cur[1]] == '0':
                        continue
                    q.append(n_cur)
            
if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))