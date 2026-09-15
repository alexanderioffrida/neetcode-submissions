class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image
        
        ROWS, COLS = len(image), len(image[0])

        def dfs(image, r, c):
            if (min(r, c) < 0 or
                r == ROWS or c == COLS
                or image[r][c] != orig):
                return
            
            image[r][c] = color
            dfs(image, r + 1, c)
            dfs(image, r - 1, c)
            dfs(image, r, c + 1)
            dfs(image, r, c - 1)
        
        dfs(image, sr, sc)
        return image