class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board[r])):
                num = board[r][c]
                if num == ".":
                    continue
                b = r//3*3 + c//3
                if num in row[r] or num in col[c] or num in box[b]:
                    return False
                row[r].add(num)
                col[c].add(num)
                box[b].add(num) 

        return True        