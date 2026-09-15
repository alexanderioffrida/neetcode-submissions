from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        if n == 1:
            return 1

        directions = [
            (-1, -1),   (-1, 0),    (-1, 1),
            (0, -1),                (0, 1),
            (1, -1),    (1, 0),     (1, 1)
        ]

        queue = deque([(0, 0, 1)])
        grid[0][0] = 1

        while queue:
            r, c, distance = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < n and 0 <= nc < n):
                    continue
                
                if grid[nr][nc] == 1:
                    continue
                
                if nr == n - 1 and nc == n - 1:
                    return distance + 1
                
                grid[nr][nc] = 1
                queue.append((nr, nc, distance + 1))
        
        return -1