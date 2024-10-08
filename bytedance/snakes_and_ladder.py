from typing import List
from collections import deque
class Solution:
    def __init__(self) -> None:
        self.board = None
        self.n = None
        self.n2 = None
    def snakesAndLadders2(self, board: List[List[int]]) -> int:
        self.n = len(board)
        self.n2 = self.n ** 2
        self.board = board
        visited = {}
        return self.search(1, visited)
    
    def search(self, i, visited):
        end_i = min(i + 7, self.n2 + 1)
        q = deque(range(i + 1, end_i))
        temp_res = 1e5
        while len(q) > 0:
            j = q.popleft()
            if j not in visited:
                visited[j] = True
                row, col = self.coor(j)
                if j == self.n2:
                    return 1
                
                if self.board[row][col] != -1:
                    visited[self.board[row][col]] = True
                    res = self.search(self.board[row][col], visited)
                    if res != -1 and res < temp_res:
                        temp_res = res
                else:
                    res = self.search(j, visited)
                    if res != -1 and res < temp_res:
                        temp_res = res
        return temp_res + 1 if temp_res < 1e5 else -1


    def coor(self, i):
        row = (i - 1) // self.n
        col = (i - 1) % self.n
        if row % 2 == 1:
            col = self.n - 1 - col
        return self.n - 1 - row, col
    
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        visited={1}
        nboard=[]
        q=[(1,0)]
        n=len(board)
        '''this loop is to rearrange the board in 2D manner'''
        for i in range(n-1,-1,-1):
            if i%2!=n%2:
                for j in range(n):
                    nboard.append(board[i][j])
            else:
                for j in range(n-1,-1,-1):
                    nboard.append(board[i][j])          
        #BFS
        while q:
            a=q.pop(0)
            for i in range(6):
                try: 
                    if nboard[a[0]+i]==-1:
                        t=a[0]+i+1
                    else:
                        t=nboard[a[0]+i]
                except:
                   break     
                if t in visited:
                    continue 
                visited.add(t)       
                if t==n*n:
                    return a[1]+1   
                q.append((t,a[1]+1))        
        return -1   

if __name__ == '__main__':
    s = Solution()
    print(s.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))