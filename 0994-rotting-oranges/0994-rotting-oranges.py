class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        oranges, ans = 0, 0
        m, n = len(grid), len(grid[0])
        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    oranges += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        if oranges == 0:
            return 0

        while q:
            ans += 1
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        oranges -= 1

        return ans - 1 if oranges == 0 else -1        