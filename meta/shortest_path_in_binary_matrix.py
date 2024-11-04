from typing import List
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        start, end = [0, 0], [len(grid) - 1, len(grid) - 1]
        direc = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        que = deque([start])
        # visited = {}
        # visited['0,0'] = 1
        grid[0][0] = 2
        while len(que) > 0:
            cur = que.popleft()
            # curkey = f'{cur[0]},{cur[1]}'
            for d in direc:
                ncur = [cur[0] + d[0], cur[1] + d[1]]
                if not (0 <= ncur[0] <= end[0] and 0 <= ncur[1] <= end[1]):
                    continue
                # ncurkey = f'{ncur[0]},{ncur[1]}'
                if ncur[0] == end[0] and ncur[1] == end[1]:
                    # return visited[curkey] + 1
                    return grid[cur[0]][cur[1]] 
                
                if grid[ncur[0]][ncur[1]] == 0:
                    que.append(ncur)
                    # visited[ncurkey] = visited[curkey] + 1
                    grid[ncur[0]][ncur[1]] = grid[cur[0]][cur[1]] + 1
        
        return grid[end[0]][end[1]] - 1