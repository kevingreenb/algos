class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        p_diag = set()
        n_diag = set()
        ans = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                copy = ["".join(r) for r in board]
                ans.append(copy)
                return
            for c in range(n):
                p_diag2 = row + c
                n_diag2 = row - c
                if c in cols or p_diag2 in p_diag or n_diag2 in n_diag:
                    continue

                cols.add(c)
                p_diag.add(p_diag2)
                n_diag.add(n_diag2)
                board[row][c] = "Q"

                backtrack(row + 1)

                cols.remove(c)
                p_diag.remove(p_diag2)
                n_diag.remove(n_diag2)
                board[row][c] = "."

        backtrack(0)
        return ans
