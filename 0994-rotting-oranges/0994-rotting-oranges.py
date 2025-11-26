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

        direction = [(1, 0), (-1, 0), (0,1), (0, -1)]

        while q:
            size = len(q)
            ans += 1
            for _ in range(size):
                r, c = q.popleft()
                for r2, c2 in direction:
                    if r+r2 < len(grid) and r+r2 >= 0 and grid[r+r2][c] == 1:
                        grid[r+r2][c] = 2
                        q.append((r+r2, c))
                        rotten += 1
                    if c+c2 < len(grid[0]) and c+c2 >= 0 and grid[r][c+c2] == 1:
                        grid[r][c+c2] = 2
                        q.append((r, c+c2))
                        rotten += 1

        return ans if oranges == rotten else -1
        