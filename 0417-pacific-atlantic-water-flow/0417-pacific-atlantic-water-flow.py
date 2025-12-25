class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        m, n = len(heights), len(heights[0])
        def explore(r, c, visited, prev):
            if 0 <= r < m and 0 <= c < n and (r, c) not in visited and heights[r][c] >= prev:
                visited.add((r, c))
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                for dr, dc in directions:
                    explore(r+dr, c+dc, visited, heights[r][c])
                    
        for c in range(n):
            explore(0, c, pac, heights[0][c])
            explore(m-1, c, atl, heights[m-1][c])

        for r in range(m):
            explore(r, 0, pac, heights[r][0])
            explore(r, n-1, atl, heights[r][n-1])

        return [[r,c] for (r, c) in pac if (r, c) in atl]
        