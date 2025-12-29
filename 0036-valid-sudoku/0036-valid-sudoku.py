class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                num = board[r][c]
                box = r//3*3 + c//3
                if num in cols[c] or num in rows[r] or num in boxes[box]:
                    return False
                cols[c].add(num)
                rows[r].add(num)
                boxes[box].add(num)
        return True