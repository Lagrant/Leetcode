class Solution:
    def __init__(self) -> None:
        self.res = 0
    def totalNQueens(self, n: int) -> int:
        def conflicts(row, col, coors):
            if len(coors) == 0:
                return False
            for c in coors:
                dist = row - c[0]
                if col == c[1] or row == c[0]:
                    return True
                if col == c[1] + dist or col == c[1] - dist:
                    return True
            return False

        def search(row, coors):
            if row >= n:
                self.res += 1
                return
            for i in range(n):
                if conflicts(row, i, coors):
                    continue
                search(row + 1, coors + [[row, i]])

        if n == 1:
            return 1
        for i in range(n):
            search(1, [[0,i]])
        return self.res
    
if __name__ == '__main__':
    s = Solution()
    print(s.totalNQueens(4))