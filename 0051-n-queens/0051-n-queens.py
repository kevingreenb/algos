class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set()
        neg_diag = set()
        ans = []
        board = [["."] * n for _ in range(n)]

        def helper(row):
            if row == n:
                copy = ["".join(r) for r in board]
                ans.append(copy)
                return
            for c in range(n):
                pos_diag2 = row + c
                neg_diag2 = row - c
                if c in cols or pos_diag2 in pos_diag or neg_diag2 in neg_diag:
                    continue
                cols.add(c)
                pos_diag.add(pos_diag2)
                neg_diag.add(neg_diag2)
                board[row][c] = "Q"
                helper(row + 1)
                cols.remove(c)
                pos_diag.remove(pos_diag2)
                neg_diag.remove(neg_diag2)                
                board[row][c] = "."

        helper(0)
        return ans
