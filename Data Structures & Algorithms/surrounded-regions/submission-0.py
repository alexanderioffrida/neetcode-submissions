class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # m x n grid
        ROWS, COLS = len(board), len(board[0])
        # connections are 4-directional (vertical or horizontal)
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]
        # we need to locate the 'O's so let's use a multi-source approach

        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if (
                    (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1)
                    and board[r][c] == "O"
                ):
                    board[r][c] = 'T'
                    queue.append((r, c))
        
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
            
                if (0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and board[nr][nc] == "O"
                ):
                    board[nr][nc] = 'T'
                    queue.append((nr, nc))
                
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"