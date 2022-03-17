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

"""
private int bit[];  // initialize all entries in bit array to 0
private int nums[]; // given nums array (ASSUME 1-based indexing)
private int n;      // size of nums array

private int lsb(int n) {
    // the line below allows us to directly capture the right most non-zero bit of a number
    return n & (-n);
}

private void updateBIT(int i, int val) {
    // keep adding lsb(i) to i and add val to bit[i]
    for (; i <= n; i += lsb(i)) {
        this.bit[i] += val;
    }
}

private int buildBIT() {
    for (int k = 1; k <= n; ++k) {
        int i = k, val = this.nums[k];
        updateBIT(i, val);
    }
}
"""

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)