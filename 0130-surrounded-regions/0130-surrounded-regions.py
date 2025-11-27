class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        def explore(r, c, board):
            if ( 
                r < 0 or c < 0 or
                r >= n or c >= m or
                board[r][c] != "O"
                ):
                return
            board[r][c] = "T"
            explore(r + 1, c, board)
            explore(r - 1, c, board)
            explore(r, c + 1, board)
            explore(r, c - 1, board)
        
        for r in range(n):
            if board[r][0] == "O":
                explore(r, 0, board)
            if board[r][m-1] == "O":
                explore(r, m-1, board)

        for c in range(1, m-1):
            if board[0][c] == "O":
                explore(0, c, board)
            if board[n-1][c] == "O":
                explore(n-1, c, board)
        
        for r in range(n):
            for c in range(m):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        