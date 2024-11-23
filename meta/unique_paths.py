class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        solution = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    solution[i][j] = 1
                    continue
                solution[i][j] = solution[i - 1][j] + solution[i][j - 1]
        return solution[-1][-1]