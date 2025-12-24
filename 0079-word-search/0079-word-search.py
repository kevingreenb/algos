class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def explore(r, c, i):
            if i == len(word):
                return True
            if (
                r < 0
                or c < 0
                or r >= len(board)
                or c >= len(board[r])
                or board[r][c] != word[i]
            ):
                return False
            temp = board[r][c]
            board[r][c] = "#"
            if (
                explore(r + 1, c, i + 1)
                or explore(r - 1, c, i + 1)
                or explore(r, c + 1, i + 1)
                or explore(r, c - 1, i + 1)
            ):
                return True
            
            board[r][c] = temp
            return False
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    if explore(r, c, 0):
                        return True
        return False
            
