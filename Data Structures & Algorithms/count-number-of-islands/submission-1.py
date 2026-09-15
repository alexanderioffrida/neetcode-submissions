class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        directions = [
            [1, 0], [-1, 0], [0, 1], [0, -1]
        ]
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            queue = deque()
            grid[r][c] = "0"
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if not (0 <= nr < ROWS and 0 <= nc < COLS):
                        continue
                    
                    if (grid[nr][nc] == "0"):

                        continue
                    
                    queue.append((nr, nc))
                    grid[nr][nc] = "0"
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1
        
        return count