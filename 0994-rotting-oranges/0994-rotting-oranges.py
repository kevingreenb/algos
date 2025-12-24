class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        oranges = 0
        rotten = 0
        ans = -1
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    oranges += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
                    
        if oranges == 0:
            return 0

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            size = len(q)
            ans += 1 
            for _ in range(size):
                r, c = q.popleft()
                
                for r2, c2 in direction:
                    nr, nc = r + r2, c + c2
                    if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                            oranges -= 1
                            
        return ans if oranges == 0 else -1
        