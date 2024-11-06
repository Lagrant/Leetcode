from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        arr = []
        i, j = 0, 0
        arr.append(mat[i][j])
        while i != m -1 or j != n - 1:
            arr1 = []
            if i == 0 or j == n - 1:
                if j < n - 1:
                    j += 1
                else:
                    i += 1
                arr1, i, j = self.move_down(mat, i, j)
            elif i == m - 1 or j == 0:
                if i < m - 1:
                    i += 1
                else:
                    j += 1
                arr1, i, j = self.move_up(mat, i, j)
            arr.extend(arr1)
        return arr
    def move_down(self, mat, i, j):
        arr = []
        while i < len(mat) and j >= 0:
            arr.append(mat[i][j])
            i += 1
            j -= 1
        i -= 1
        j += 1
        return arr, i, j
    def move_up(self, mat, i, j):
        arr = []
        while i >= 0 and j < len(mat[0]):
            arr.append(mat[i][j])
            i -= 1
            j += 1
        i += 1
        j -= 1
        return arr, i, j

if __name__  == '__main__':
    s = Solution()
    print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))