class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def explore(b, r, c, old, new):
            if r < 0 or c < 0 or r >= len(b) or c >= len(b[r]) or b[r][c] != old:
                return
            b[r][c] = new
            explore(b, r + 1, c, old, new)
            explore(b, r - 1, c, old, new)
            explore(b, r, c + 1, old, new)
            explore(b, r, c - 1, old, new)

        for r in range(len(board)):
            explore(board, r, 0, "O", "T")
            explore(board, r, len(board[r])-1, "O", "T")

        for c in range(len(board[0])):
            explore(board, 0, c, "O", "T")
            explore(board, len(board)-1, c, "O", "T")

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        