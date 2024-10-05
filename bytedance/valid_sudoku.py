from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for bd in board:
            rec = {}
            for b in bd:
                if b == '.':
                    continue
                if b in rec:
                    return False
                rec[b] = 1
        for i in range(9):
            rec = {}
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in rec:
                    return False
                rec[board[j][i]] = 1
        for i in range(9):
            rec = {}
            row = i // 3 * 3
            col = i % 3 * 3
            for j in range(9):
                srow = j // 3 + row
                scol = j % 3 + col
                if board[srow][scol] == '.':
                    continue
                if board[srow][scol] in rec:
                    return False
                rec[board[srow][scol]] = 1
        return True
    
if __name__ == '__main__':
    s = Solution()
    print(s.isValidSudoku([
                        [".",".",".",".","5",".",".","1","."],\
                        [".","4",".","3",".",".",".",".","."],\
                        [".",".",".",".",".","3",".",".","1"],\
                        ["8",".",".",".",".",".",".","2","."],\
                        [".",".","2",".","7",".",".",".","."],\
                        [".","1","5",".",".",".",".",".","."],\
                        [".",".",".",".",".","2",".",".","."],\
                        [".","2",".","9",".",".",".",".","."],\
                        [".",".","4",".",".",".",".",".","."]]))
