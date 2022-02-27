class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix) - 1
        start = [0,0]   # y, x
        temp = 1001
        while (size > 0):
            for i in range(size):
                temp = matrix[start[0] + i][start[1] + size]

                matrix[start[0] + i][start[1] + size] = matrix[start[0]][start[1] + i]
                matrix[start[0] + size][start[1] + size - i], temp = temp, matrix[start[0] + size][start[1] + size - i]
                matrix[start[0] + size - i][start[1]], temp = temp,  matrix[start[0] + size - i][start[1]]
                matrix[start[0]][start[1] + i] = temp
            size -= 2
            start[0] += 1
            start[1] += 1
                
sol = Solution()
sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])