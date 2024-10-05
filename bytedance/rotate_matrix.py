from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        end = (len(matrix) - 1) // 2 + 1
        cnt = 0
        while cnt < end:
            l_1 = len(matrix) - cnt - 1
            lm_1 = len(matrix) - 1
            for i in range(cnt, l_1):
                matrix[cnt][i], matrix[i][l_1] = matrix[i][l_1], matrix[cnt][i]
                matrix[cnt][i], matrix[l_1][lm_1 - i] = matrix[l_1][lm_1 - i], matrix[cnt][i]
                matrix[cnt][i], matrix[lm_1 - i][cnt] = matrix[lm_1 - i][cnt], matrix[cnt][i]
            cnt += 1