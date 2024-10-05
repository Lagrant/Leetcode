from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r_count, c_count = {}, {}
        for i, _  in enumerate(matrix):
            for j, _ in enumerate(matrix[0]):
                if matrix[i][j] == 0:
                    r_count[i] = 0
                    c_count[j] = 0
        for r in r_count:
            for j, _ in enumerate(matrix[0]):
                matrix[r][j] = 0
        for c in c_count:
            for i, _ in enumerate(matrix):
                matrix[i][c] = 0