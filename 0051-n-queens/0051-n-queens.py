class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, pos_d, neg_d = set(), set(), set()
        board = [["." for _ in range(n)] for _ in range(n)]
        ans = []
        def helper(r):
            if r == n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return
            for c in range(len(board[r])):
                if c in cols:
                    continue
                elif r + c in pos_d:
                    continue
                elif r - c in neg_d:
                    continue
                board[r][c] = "Q"
                cols.add(c)
                pos_d.add(r + c)
                neg_d.add(r - c)
                helper(r + 1)
                board[r][c] = "."
                cols.remove(c)
                pos_d.remove(r + c)
                neg_d.remove(r - c)
        helper(0)
        return ans                
