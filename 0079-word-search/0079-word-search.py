class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def explore(i, r, c):
            if i >= len(word):
                return True
    
            if r < 0 or c < 0 or r >= m or c >= n or word[i] != board[r][c]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            if (
                explore(i + 1, r + 1, c) or
                explore(i + 1, r - 1, c) or 
                explore(i + 1, r, c + 1) or
                explore(i + 1, r, c - 1)
            ):
                return True

            board[r][c] = temp
            return False
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and explore(0, r, c):
                    return True
                    
        return False
