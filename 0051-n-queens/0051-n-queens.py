from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diags = set() 
        neg_diags = set()
        
        res = []
        board = [["."] * n for _ in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                cur_pos_diag = r + c
                cur_neg_diag = r - c
                
                if (c in cols or 
                    cur_pos_diag in pos_diags or 
                    cur_neg_diag in neg_diags):
                    continue
                
                cols.add(c)
                pos_diags.add(cur_pos_diag)
                neg_diags.add(cur_neg_diag)
                board[r][c] = "Q"
                
                backtrack(r + 1)
                
                cols.remove(c)
                pos_diags.remove(cur_pos_diag)
                neg_diags.remove(cur_neg_diag)
                board[r][c] = "."
        
        backtrack(0)
        return res