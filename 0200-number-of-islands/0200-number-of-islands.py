class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def explore(r, c, grid):
            if (
                r < 0
                or c < 0
                or r >= len(grid)
                or c >= len(grid[r])
                or grid[r][c] != "1"
            ):
                return 0
            grid[r][c] = "0"
            explore(r - 1, c, grid)
            explore(r + 1, c, grid)
            explore(r, c - 1, grid)
            explore(r, c + 1, grid)

        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    ans += 1
                    explore(r, c, grid)
                    
        return ans
