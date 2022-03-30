class Solution:
    def removeOnes(self, grid) -> bool:
        for i in range(1, len(grid)):
            if not self.same(grid[i], grid[0]) and not self.canflip(grid[i], grid[0]):
                return False
        return True

    def same(self, row1, row2):
        for r1, r2 in zip(row1, row2):
            if r1 != r2:
                return False
        return True
    
    def canflip(self, row1, row2):
        for r1, r2 in zip(row1, row2):
            if r1 + r2 != 1:
                return False
        
        return True