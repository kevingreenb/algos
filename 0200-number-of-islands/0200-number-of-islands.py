class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def explore(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] == "1":
                grid[r][c] = "0"
                dir = [(0, 1), (0,-1), (1,0), (-1, 0)]
                for dr, dc in dir:
                    explore(r + dr, c + dc)
        ans = 0 
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    ans += 1
                    explore(r, c)
        return ans
        