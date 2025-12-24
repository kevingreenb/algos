class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def explore(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            ans = 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for r2, c2 in directions:
                ans += explore(r + r2, c + c2)
            return ans
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    ans = max(ans, explore(r, c))
        return ans