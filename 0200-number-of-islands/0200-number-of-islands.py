class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def explore(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            explore(r + 1, c)
            explore(r - 1, c)
            explore(r, c + 1)
            explore(r, c - 1)

        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    ans += 1
                    explore(r, c)
        return ans