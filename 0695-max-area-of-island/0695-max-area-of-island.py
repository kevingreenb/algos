class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def explore(r, c, grid):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] != 1:
                return 0

            grid[r][c] = 0
            left = explore(r + 1, c, grid)
            right = explore(r - 1, c, grid)
            up = explore(r, c + 1, grid)
            down = explore(r, c - 1, grid)

            return 1 + left + right + up + down

        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    ans = max(ans, explore(r, c, grid))
        return ans
