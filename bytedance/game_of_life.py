from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 1 and len(board[0]) == 1:
            board[0][0] = 0
            return
        if len(board) == 1:
            if len(board[0]) == 2:
                board[0][0] = 0
                board[0][1] = 0
                return
            for i in range(1, len(board[0]) - 1):
                if not ((board[0][i - 1] == 1 or board[0][i - 1] == -1) and (board[0][i + 1] == 1 or board[0][i + 1] == -1)):
                #     board[0][i] = 1 if board[0][i] == 1 else 2
                # else:
                    board[0][i] = 0 if board[0][i] == 0 else -1
            for i in range(1, len(board[0]) - 1):
                if board[0][i] == 2:
                    board[0][i] = 1
                elif board[0][i] == -1:
                    board[0][i] = 0
            board[0][0] = board[0][-1] = 0
            return
        if len(board[0]) == 1:
            if len(board) == 2:
                board[0][0] = 0
                board[1][0] = 0
                return
            for i in range(1, len(board) - 1):
                if not ((board[i - 1][0] == 1 or board[i - 1][0] == -1) and (board[i + 1][0] == 1 or board[i + 1][0] == -1)):
                #     board[i][0] = 1 if board[i][0] == 1 else 2
                # else:
                    board[i][0] = 0 if board[i][0] == 0 else -1
            for i in range(1, len(board) - 1):
                if board[i][0] == 2:
                    board[i][0] = 1
                elif board[i][0] == -1:
                    board[i][0] = 0
            board[0][0] = board[-1][0] = 0
            return
        
        for i, _ in enumerate(board):
            for j, _ in enumerate(board[0]):
                if i == 0 and j == 0:
                    neig = [
                            1 if board[i + 1][j] == 1 or board[i + 1][j] == -1 else 0, \
                            1 if board[i][j + 1] == 1 or board[i][j + 1] == -1 else 0, \
                            1 if board[i + 1][j + 1] == 1 or board[i + 1][j + 1] == -1 else 0]
                elif i == 0 and j == len(board[0]) - 1:
                    neig = [
                            1 if board[i + 1][j] == 1 or board[i + 1][j] == -1 else 0, \
                            1 if board[i][j - 1] == 1 or board[i][j - 1] == -1 else 0, \
                            1 if board[i + 1][j - 1] == 1 or board[i + 1][j - 1] == -1 else 0]
                elif i == len(board) - 1 and j == 0:
                    neig = [
                            1 if board[i - 1][j] == 1 or board[i - 1][j] == -1 else 0, \
                            1 if board[i][j + 1] == 1 or board[i][j + 1] == -1 else 0, \
                            1 if board[i - 1][j + 1] == 1 or board[i - 1][j + 1] == -1 else 0]
                elif i == len(board) - 1 and j == len(board[0]) - 1:
                    neig = [
                            1 if board[i - 1][j] == 1 or board[i - 1][j] == -1 else 0, \
                            1 if board[i][j - 1] == 1 or board[i][j - 1] == -1 else 0, \
                            1 if board[i - 1][j - 1] == 1 or board[i - 1][j - 1] == -1 else 0]
                elif i == 0:
                    neig = [
                            1 if board[i + 1][j] == 1 or board[i + 1][j] == -1 else 0, \
                            1 if board[i][j + 1] == 1 or board[i][j + 1] == -1 else 0, \
                            1 if board[i + 1][j + 1] == 1 or board[i + 1][j + 1] == -1 else 0,\
                            1 if board[i][j - 1] == 1 or board[i][j - 1] == -1 else 0, \
                            1 if board[i + 1][j - 1] == 1 or board[i + 1][j - 1] == -1 else 0]
                elif i == len(board) - 1:
                    neig = [
                            1 if board[i - 1][j] == 1 or board[i - 1][j] == -1 else 0, \
                            1 if board[i][j + 1] == 1 or board[i][j + 1] == -1 else 0, \
                            1 if board[i - 1][j + 1] == 1 or board[i - 1][j + 1] == -1 else 0, \
                            1 if board[i][j - 1] == 1 or board[i][j - 1] == -1 else 0, \
                            1 if board[i - 1][j - 1] == 1 or board[i - 1][j - 1] == -1 else 0]
                elif j == 0:
                    neig = [
                            1 if board[i + 1][j] == 1 or board[i + 1][j] == -1 else 0, \
                            1 if board[i][j + 1] == 1 or board[i][j + 1] == -1 else 0, \
                            1 if board[i + 1][j + 1] == 1 or board[i + 1][j + 1] == -1 else 0, \
                            1 if board[i - 1][j] == 1 or board[i - 1][j] == -1 else 0, \
                            1 if board[i - 1][j + 1] == 1 or board[i - 1][j + 1] == -1 else 0]
                elif j == len(board[0]) - 1:
                    neig = [
                            1 if board[i + 1][j] == 1 or board[i + 1][j] == -1 else 0, \
                            1 if board[i][j - 1] == 1 or board[i][j - 1] == -1 else 0, \
                            1 if board[i + 1][j - 1] == 1 or board[i + 1][j - 1] == -1 else 0, \
                            1 if board[i - 1][j] == 1 or board[i - 1][j] == -1 else 0, \
                            1 if board[i - 1][j - 1] == 1 or board[i - 1][j - 1] == -1 else 0]
                else:
                    neig = [
                            1 if board[i - 1][j] == 1 or board[i - 1][j] == -1 else 0, \
                            1 if board[i][j - 1] == 1 or board[i][j - 1] == -1 else 0, \
                            1 if board[i - 1][j - 1] == 1 or board[i - 1][j - 1] == -1 else 0,\
                            1 if board[i + 1][j] == 1 or board[i + 1][j] == -1 else 0, \
                            1 if board[i][j + 1] == 1 or board[i][j + 1] == -1 else 0, \
                            1 if board[i + 1][j + 1] == 1 or board[i + 1][j + 1] == -1 else 0,\
                            1 if board[i - 1][j + 1] == 1 or board[i - 1][j + 1] == -1 else 0,\
                            1 if board[i + 1][j - 1] == 1 or board[i + 1][j - 1] == -1 else 0]
                sneig = sum(neig)
                if sneig <= 1 or sneig >= 4:
                    board[i][j] = 0 if board[i][j] == 0 else -1
                elif sneig == 3:
                    board[i][j] = 1 if board[i][j] == 1 else 2
        for i, _ in enumerate(board):
            for j, _ in enumerate(board[0]):
                board[i][j] = 0 if board[i][j] == 0 or board[i][j] == -1 else 1

if __name__ == '__main__':
    s = Solution()
    b = [[1,0,0,1]]
    s.gameOfLife(b)
    print(b)