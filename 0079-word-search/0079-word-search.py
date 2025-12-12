class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[i]:
                return False
            temp = board[r][c]
            board[r][c] = "#"
            if dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1):
                return True
            board[r][c] = temp
            return False

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False