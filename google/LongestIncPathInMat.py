class Solution:
    def __init__(self) -> None:
        self.longest = 1
        self.cnt_map = None
    
    def longestIncreasingPath(self, matrix) -> int:
        self.cnt_map = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (self.cnt_map[i][j] != 0):
                    continue
                cur_path = [[i,j]]
                self.cnt_map[i][j] = 1
                self.subPath(cur_path, matrix)
        
        # print(self.longest)
        return self.longest

    def subPath(self, cur_path, matrix):
        i, j = cur_path[-1]
        cur_path_len = len(cur_path)
        max_temp = [self.cnt_map[cur_path[-1][0]][cur_path[-1][1]]] * 4
        if (i > 0 and matrix[i-1][j] > matrix[i][j]):
            if (self.cnt_map[i-1][j] != 0):
                # self.cnt_map[i][j] = self.cnt_map[i-1][j] + 1
                max_temp[0] = self.cnt_map[i-1][j] + 1
                # if (self.cnt_map[i][j] > self.longest):
                    # self.longest = self.cnt_map[i][j]
            else:
                self.cnt_map[i-1][j] = 1
                cur_path.append([i-1, j])
                max_temp[0] += self.subPath(cur_path, matrix)
                # sub_path = cur_path[cur_path_len:]
                cur_path = cur_path[:cur_path_len]
                # self.cnt_map[cur_path[-1][0]][cur_path[-1][1]] += len(sub_path)
                # max_temp[0] += len(sub_path)
                # if (self.cnt_map[cur_path[-1][0]][cur_path[-1][1]] > self.longest):
                #     self.longest = self.cnt_map[cur_path[-1][0]][cur_path[-1][1]]
                # for k in range(len(sub_path)):
                #     self.cnt_map[sub_path[len(sub_path) - 1 - k][0]][sub_path[len(sub_path) - 1 - k][1]] += k
                #     if (self.cnt_map[sub_path[len(sub_path) - 1 - k][0]][sub_path[len(sub_path) - 1 - k][1]] > self.longest):
                #         self.longest = self.cnt_map[sub_path[len(sub_path) - 1 - k][0]][sub_path[len(sub_path) - 1 - k][1]]
                
        if (i < len(matrix) - 1 and matrix[i+1][j] > matrix[i][j]):
            if (self.cnt_map[i+1][j] != 0):
                # self.cnt_map[i][j] = self.cnt_map[i+1][j] + 1
                max_temp[1] = self.cnt_map[i+1][j] + 1
                # if (self.cnt_map[i][j] > self.longest):
                    # self.longest = self.cnt_map[i][j]
            else:
                self.cnt_map[i+1][j] = 1
                cur_path.append([i+1, j])
                max_temp[1] += self.subPath(cur_path, matrix)
                # sub_path = cur_path[cur_path_len:]
                cur_path = cur_path[:cur_path_len]
                # self.cnt_map[cur_path[-1][0]][cur_path[-1][1]] += len(sub_path)
                # max_temp[1] += len(sub_path)
                # if (self.cnt_map[cur_path[-1][0]][cur_path[-1][1]] > self.longest):
                #     self.longest = self.cnt_map[cur_path[-1][0]][cur_path[-1][1]]
                # for k in range(len(sub_path)):
                #     self.cnt_map[sub_path[len(sub_path) - 1 - k][0]][sub_path[len(sub_path) - 1 - k][1]] += k
                #     if (self.cnt_map[sub_path[len(sub_path) - 1 - k][0]][sub_path[len(sub_path) - 1 - k][1]] > self.longest):
                #         self.longest = self.cnt_map[sub_path[len(sub_path) - 1 - k][0]][sub_path[len(sub_path) - 1 - k][1]]
                

        if (j > 0 and matrix[i][j-1] > matrix[i][j]):
            if (self.cnt_map[i][j-1] != 0):
                # self.cnt_map[i][j] = self.cnt_map[i][j-1] + 1
                max_temp[2] = self.cnt_map[i][j-1] + 1
                # if (self.cnt_map[i][j] > self.longest):
                    # self.longest = self.cnt_map[i][j]
            else:
                self.cnt_map[i][j-1] = 1
                cur_path.append([i,j-1])
                max_temp[2] += self.subPath(cur_path, matrix)
                # sub_path = cur_path[cur_path_len:]
                cur_path = cur_path[:cur_path_len]
                # self.cnt_map[cur_path[-1][0]][cur_path[-1][1]] += len(sub_path)
                # max_temp[2] += len(sub_path)
                # if (self.cnt_map[cur_path[-1][0]][cur_path[-1][1]] > self.longest):
                #     self.longest = self.cnt_map[cur_path[-1][0]][cur_path[-1][1]]
                # for k in range(len(sub_path)):
                #     self.cnt_map[sub_path[len(sub_path) - 1 - k][0]][sub_path[len(sub_path) - 1 - k][1]] += k
                #     if (self.cnt_map[sub_path[len(sub_path) - 1 - k][0]][sub_path[len(sub_path) - 1 - k][1]] > self.longest):
                #         self.longest = self.cnt_map[sub_path[len(sub_path) - 1 - k][0]][sub_path[len(sub_path) - 1 - k][1]]
                
                
        if (j < len(matrix[0]) - 1 and matrix[i][j+1] > matrix[i][j]):
            if (self.cnt_map[i][j+1] != 0):
                # self.cnt_map[i][j] = self.cnt_map[i][j+1] + 1
                max_temp[3] = self.cnt_map[i][j+1] + 1
                # if (self.cnt_map[i][j] > self.longest):
                    # self.longest = self.cnt_map[i][j]
            else:
                self.cnt_map[i][j+1] = 1
                cur_path.append([i,j+1])
                max_temp[3] += self.subPath(cur_path, matrix)
                # sub_path = cur_path[cur_path_len:]
                cur_path = cur_path[:cur_path_len]
                # self.cnt_map[cur_path[-1][0]][cur_path[-1][1]] += len(sub_path)
                # max_temp[3] += len(sub_path)
                # if (self.cnt_map[cur_path[-1][0]][cur_path[-1][1]] > self.longest):
                #     self.longest = self.cnt_map[cur_path[-1][0]][cur_path[-1][1]]
                # for k in range(len(sub_path)):
                    # self.cnt_map[sub_path[len(sub_path) - 1 - k][0]][sub_path[len(sub_path) - 1 - k][1]] += k
                    # if (self.cnt_map[sub_path[len(sub_path) - 1 - k][0]][sub_path[len(sub_path) - 1 - k][1]] > self.longest):
                        # self.longest = self.cnt_map[sub_path[len(sub_path) - 1 - k][0]][sub_path[len(sub_path) - 1 - k][1]]
        self.cnt_map[i][j] = max(*max_temp)
        if (self.cnt_map[i][j] > self.longest):
            self.longest = self.cnt_map[i][j]
        return self.cnt_map[i][j]

sol = Solution()
print(sol.longestIncreasingPath([[1,2],[2,3]]))