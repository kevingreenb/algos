class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(r, c, heights, visited, previous):
            if (
                r < 0
                or c < 0
                or r >= len(heights)
                or c >= len(heights[r])
                or (r, c) in visited
                or heights[r][c] <= previous
            ):
                return
            visited.add((r,c))
            dfs(r - 1, c, heights, visited, heights[r][c])
            dfs(r + 1, c, heights, visited, heights[r][c])
            dfs(r, c - 1, heights, visited, heights[r][c])
            dfs(r, c + 1, heights, visited, heights[r][c])

        atl, pac = set(), set()
        n, m = len(heights), len(heights[0])

        for r in range(n):
            dfs(r, 0, heights, pac, heights[r][0])
            dfs(r, m - 1, heights, atl, heights[r][m - 1])

        for c in range(m):
            dfs(0, c, heights, pac, heights[0][c])
            dfs(n - 1, c, heights, atl, heights[n - 1][c])

        ans = []
        for cell in pac:
            if cell in atl:
                ans.append(cell)
        
        return ans