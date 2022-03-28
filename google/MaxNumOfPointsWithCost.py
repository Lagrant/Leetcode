class Solution:
    def maxPoints(self, points) -> int:
        point_matrix = [0] * len(points[0])

        for i in range(len(points)):
            new_pm = point_matrix[:]
            for j in range(1, len(points[i])):
                new_pm[j] = max(new_pm[j-1] - 1, new_pm[j])
            for j in range(len(points[i]) - 2, -1, -1):
                new_pm[j] = max(new_pm[j+1] - 1, new_pm[j])
            point_matrix = [points[i][j] + new_pm[j] for j in range(len(points[i]))]

        return max(point_matrix)

sol = Solution()
print(sol.maxPoints([[0,3,0,4,2],[5,4,2,4,1],[5,0,0,5,1],[2,0,1,0,3]]))