class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cs = defaultdict(set)
        rs = defaultdict(set)
        sqs = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rs[r]
                    or board[r][c] in cs[c]
                    or board[r][c] in sqs[(r // 3, c // 3)]):
                    return False
                
                cs[c].add(board[r][c])
                rs[r].add(board[r][c])
                sqs[(r // 3, c // 3)].add(board[r][c])
        
        return True