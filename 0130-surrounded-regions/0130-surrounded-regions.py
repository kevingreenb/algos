class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def explore(r, c):
            if 0 <= r < m and 0 <= c < n and board[r][c] == "O":
                board[r][c] = "T"
                directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    explore(r + dr, c + dc)
        for r in range(m):
            explore(r, 0)
            explore(r, n-1)

        for c in range(n):
            explore(0, c)
            explore(m-1, c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        