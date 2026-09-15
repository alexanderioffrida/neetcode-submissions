class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use HashTable –– insert / delete / search (O(1) avg.) operations
        # dictionary –– mapping keys to values
        # HashTable –– implementing dictionary with hash function
        # Direct-Access Tables –– universe of keys / actual keys –– array
        # HashTable Space Req.: O(K)
            # two different keys --> same value: collision
            # accomodate via chaining by linked lists for value buckets
            # we need to maximize randomness and produce the least amount of collisions
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == '.':
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        
        for sq in range(9):
            seen = set()
            for i in range (3):
                for j in range(3):
                    row = (sq//3) * 3 + i
                    col = (sq % 3) * 3 + j
                    if board [row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True


