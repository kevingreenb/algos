class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self.adj_cache = {}
        self.diag_cache = {}
        self._precompute(grid)

    def _precompute(self, grid):
        n = len(grid)
        # (row_offset, col_offset)
        adj_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for r in range(n):
            for c in range(n):
                val = grid[r][c]
                self.adj_cache[val] = self._get_sum(grid, r, c, adj_dirs)
                self.diag_cache[val] = self._get_sum(grid, r, c, diag_dirs)

    def _get_sum(self, grid, r, c, dirs):
        n = len(grid)
        total = 0
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                total += grid[nr][nc]
        return total

    def adjacentSum(self, value):
        return self.adj_cache.get(value, 0)

    def diagonalSum(self, value):
        return self.diag_cache.get(value, 0)


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
