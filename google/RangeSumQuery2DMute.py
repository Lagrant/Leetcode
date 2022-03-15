class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.sum_matrix = [[0] * len(self.matrix[0])] * len(self.matrix)

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        accu = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                accu += self.matrix[i][j]
        return accu

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)