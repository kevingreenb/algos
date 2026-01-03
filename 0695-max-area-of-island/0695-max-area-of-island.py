class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def explore(r, c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                grid[r][c] = 0
                ans = 1
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for r2, c2 in directions:
                    ans += explore(r + r2, c + c2)
                return ans
            return 0
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans = max(ans, explore(r, c))
        return ans