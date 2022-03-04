class Solution:
    def __init__(self) -> None:
        self.num = 0
    def numIslands(self, grid) -> int:
        visitMap = [[1] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == '1' and visitMap[i][j] == 1):
                    self.findIsland([i,j], grid, visitMap)
                    self.num += 1
        
        return self.num

    def findIsland(self, cur, grid, visitMap):
        visitMap[cur[0]][cur[1]] -= 1
        if (grid[cur[0]][cur[1]] == '0'):
            return
        
        if (cur[0] > 0):
            if (visitMap[cur[0] - 1][cur[1]] == 1):
                self.findIsland([cur[0]  - 1, cur[1]], grid, visitMap)
        if (cur[0] < len(grid) - 1):
            if (visitMap[cur[0] + 1][cur[1]] == 1):
                self.findIsland([cur[0] + 1, cur[1]], grid, visitMap)
        if (cur[1] > 0):
            if (visitMap[cur[0]][cur[1] - 1] == 1):
                self.findIsland([cur[0], cur[1] - 1], grid, visitMap)
        if (cur[1] < len(grid[0]) - 1):
            if (visitMap[cur[0]][cur[1] + 1] == 1):
                self.findIsland([cur[0], cur[1] + 1], grid, visitMap)
        
        # visitMap[cur[0]][cur[1]] -= 1

        return