from typing import List
class Solution:
    def __init__(self) -> None:
        self.visited = {}
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(n):
            if board[0][i] == 'O':
                self.connect(board, 0, i)
            if board[-1][i] == 'O':
                self.connect(board, m - 1, i)
        for i in range(m):
            if board[i][0] == 'O':
                self.connect(board, i, 0)
            if board[i][-1] == 'O':
                self.connect(board, i, n - 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and f'{i},{j}' not in self.visited:
                    board[i][j] = 'X'

    def connect(self, board, i, j):
        if f'{i},{j}' in self.visited:
            return
        self.visited[f'{i},{j}'] = True
        direc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        q = [[i, j]]
        while len(q) > 0:
            cur = q.pop()
            for d in direc:
                n_cur = [d[0] + cur[0], d[1] + cur[1]]
                if 0 <= n_cur[0] < len(board) and 0 <= n_cur[1] < len(board[0]):
                    if board[n_cur[0]][n_cur[1]] ==  'O':
                        if f'{n_cur[0]},{n_cur[1]}' not in self.visited:
                            q.append(n_cur)
                            self.visited[f'{n_cur[0]},{n_cur[1]}'] = True