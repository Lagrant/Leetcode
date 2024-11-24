from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        direc = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        visited = set()
        que = deque()
        que.append((0, 0, 0))
        visited.add((0, 0))
        while que:
            cur_x, cur_y, steps = que.popleft()
            if cur_x == x and cur_y == y:
                return steps
            for dx, dy in direc:
                new_x, new_y = cur_x + dx, cur_y + dy
                if -1 <= new_x <= x + 2 and -1 <= new_y <= y + 2 and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    que.append((new_x, new_y, steps + 1))
        return -1