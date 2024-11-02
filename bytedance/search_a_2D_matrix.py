from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        k = self.search_row(matrix, m, target)
        if k == 'true':
            return True
        return self.search_col(matrix, n, k, target)

    def search_row(self, matrix, m, target):
        i, j = 0, m
        while abs(i - j) > 1:
            mid = (i + j) // 2
            if matrix[mid][0] == target:
                return 'true'
            if matrix[mid][0] < target:
                i = mid
            else:
                j = mid
        
        i, j = min(i, j), max(i, j)
        return j if target >= matrix[j][0] else i
    
    def search_col(self, matrix, n, k, target):
        i, j = 0, n
        while abs(i - j) > 1:
            mid = (i + j) // 2
            if matrix[k][mid] == target:
                return True
            if matrix[k][mid] < target:
                i = mid
            else:
                j = mid
        
        return True if matrix[k][i] == target or matrix[k][j] == target else False
    
if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1], [3]], 3))