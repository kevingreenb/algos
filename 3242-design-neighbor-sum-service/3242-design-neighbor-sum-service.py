class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.adj_cache = {}
        self.diag_cache = {}
        self.compute_adj_grid(grid)
        self.compute_diag_grid(grid)

    def compute_adj_grid(self, grid) -> None:
        for r in range(len(grid)):
            for c in range(len(grid[r])):

                up = grid[r - 1][c] if r > 0 else 0
                down = grid[r + 1][c] if r + 1 < len(grid) else 0
                left = grid[r][c - 1] if c > 0 else 0
                right = grid[r][c + 1] if c + 1 < len(grid[r]) else 0

                self.adj_cache[grid[r][c]] = up + down + left + right

    def compute_diag_grid(self, grid) -> None:
        for r in range(len(grid)):
            for c in range(len(grid[r])):

                up_left = grid[r - 1][c - 1] if r > 0 and c > 0 else 0
                down_left = grid[r + 1][c - 1] if r + 1 < len(grid) and c > 0 else 0
                up_right = grid[r - 1][c + 1] if r > 0 and c + 1 < len(grid) else 0
                down_right = (
                    grid[r + 1][c + 1] if r + 1 < len(grid) and c + 1 < len(grid) else 0
                )

                self.diag_cache[grid[r][c]] = up_left + down_left + up_right + down_right

    def adjacentSum(self, value: int) -> int:
        return self.adj_cache[value]

    def diagonalSum(self, value: int) -> int:
        return self.diag_cache[value]


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
