from typing import List
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        n = len(grid)
        if n == 1:
            return Node(grid[0][0] == 1, True, None, None, None, None)
        if n == 2:
            if grid[0][0] == grid[0][1] == grid[1][0] == grid[1][1]:
                return Node(grid[0][0] == 1, True, None, None, None, None)

        subn = n // 2
        t = grid[:subn]
        b = grid[subn:]
        tl, tr = [], []
        bl, br = [], []
        for trow in t:
            tl.append(trow[:subn])
            tr.append(trow[subn:])
        for brow in b:
            bl.append(brow[:subn])
            br.append(brow[subn:])
        nodetl = self.construct(tl)
        nodetr = self.construct(tr)
        nodebl = self.construct(bl)
        nodebr = self.construct(br)
        if nodetl.isLeaf and nodetr.isLeaf and nodebl.isLeaf and nodebr.isLeaf and nodetl.val == nodetr.val == nodebl.val == nodebr.val:
            return Node(nodetl.val, True, None, None, None, None)
        else:
            return Node(False, False, nodetl, nodetr, nodebl, nodebr)
    
if __name__ == '__main__':
    s = Solution()
    grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    print(s.construct(grid))