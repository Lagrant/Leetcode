from typing import List
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        if board[click[0]][click[1]] == 'E':
            self.search_adj(board, click)
        
        return board
    
    def count_neighs(self, board, c):
        cnt = 0
        direc = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        for d in direc:
            cadj = [c[0] + d[0], c[1] + d[1]]
            if 0<= cadj[0] < len(board) and 0 <= cadj[1] < len(board[0]) and board[cadj[0]][cadj[1]] == 'M':
                cnt += 1
        return cnt

    def search_adj(self, board, c):
        if board[c[0]][c[1]] == 'B' or '1' <= board[c[0]][c[1]] <= '8':
            return

        num_neigh = self.count_neighs(board, c)
        if num_neigh > 0:
            board[c[0]][c[1]] = str(num_neigh)
            return
        board[c[0]][c[1]] = 'B'
        direc = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        for d in direc:
            cadj = [c[0] + d[0], c[1] + d[1]]
            if cadj[0] < 0 or cadj[0] >= len(board) or cadj[1] < 0 or cadj[1] >= len(board[0]):
                continue
            if board[cadj[0]][cadj[1]] == 'B' or '1' <= board[cadj[0]][cadj[1]] <= '8':
                continue
            self.search_adj(board, cadj)