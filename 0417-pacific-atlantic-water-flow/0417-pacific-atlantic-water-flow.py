class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ans = []
        n, m = len(heights), len(heights[0])

        def explore(r, c, heights, visited, prev):
            if (
                r < 0
                or c < 0
                or r >= len(heights)
                or c >= len(heights[r])
                or heights[r][c] < prev
                or (r, c) in visited
            ):
                return
            visited.add((r, c))
            explore(r - 1, c, heights, visited, heights[r][c])
            explore(r + 1, c, heights, visited, heights[r][c])
            explore(r, c - 1, heights, visited, heights[r][c])
            explore(r, c + 1, heights, visited, heights[r][c])
        
        for r in range(n):
            explore(r, 0, heights, pac, heights[r][0])
            explore(r, m-1, heights, atl, heights[r][m-1])

        for c in range(m):
            explore(0, c, heights, pac, heights[0][c])
            explore(n-1, c, heights, atl, heights[n-1][c])
        
        for element in pac:
            if element in atl:
                ans.append([element[0],element[1]])
        
        return ans