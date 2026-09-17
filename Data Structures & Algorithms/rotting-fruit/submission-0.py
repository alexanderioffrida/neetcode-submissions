class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs as implementation to go level-by-level.
        # each level corresponds to a minute.

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque() # rotten queue
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        minutes = 0
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < ROWS and 0 <= nc < COLS
                        and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1
        
        return minutes if fresh == 0 else -1
                        

