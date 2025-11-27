class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()

        def explore(r, c, heights, visited, prev):
            if (
                r < 0
                or c < 0
                or r >= len(heights)
                or c >= len(heights[r])
                or heights[r][c] <= prev
                or heights[r][c] in visited
            ):
                return
            visited.add((r, c))
            explore(r, c, heights, visited, prev)
            explore(r, c, heights, visited, prev)

