from typing import List
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(n):
            t = matrix[0][i]
            for j in range(i, n):
                if j - i >= m:
                    break
                if matrix[j - i][j] != t:
                    return False
        for i in range(1, m):
            t = matrix[i][0]
            for j in range(i, m):
                if j - i >= n:
                    break
                if matrix[j][j - i] !=t:
                    return False
        return True
    
    def isToeplitzMatrix1(self, matrix: List[List[int]]) -> bool:
        # for i in range(1,len(matrix)):
        #     for j in range(1,len(matrix[0])):
        #         if matrix[i-1][j-1] != matrix[i][j]:
        #             return False
        # return True
        prev = matrix[0]
        for i in range(1,len(matrix)):
            prev.pop()
            if matrix[i][1:] != prev:
                return False
            prev = matrix[i]
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isToeplitzMatrix([[11,74,0,93],[40,11,74,7]]))