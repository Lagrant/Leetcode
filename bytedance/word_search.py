from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(word, coor, visited):
            if len(word) == 0:
                return True
            for d in direc:
                try:
                    n_coor = [coor[0] + d[0], coor[1] + d[1]]
                    if n_coor[0] < 0 or n_coor[1] < 0:
                        continue

                    if f'{n_coor[0]},{n_coor[1]}' not in visited:
                        if board[n_coor[0]][n_coor[1]] == word[0]:
                            visited[f'{n_coor[0]},{n_coor[1]}'] = True
                            res = search(word[1:], n_coor, visited)
                            del visited[f'{n_coor[0]},{n_coor[1]}']
                            if res:
                                return True
                except IndexError:
                    continue
            return False

        direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    res = search(word[1:], [i, j], {f'{i},{j}':True})
                    if res:
                        return True
        return False
    
if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))