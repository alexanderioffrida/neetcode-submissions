class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def bfs(r, c):
            cur_area = 1
            queue = deque([(r, c)])
            grid[r][c] = 0

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if not (0 <= nr < ROWS and 0 <= nc < COLS):
                        continue
                    
                    if (grid[nr][nc] == 0):
                        continue
                    
                    grid[nr][nc] = 0
                    queue.append((nr, nc))
                    cur_area += 1
            
            return cur_area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area
                    


