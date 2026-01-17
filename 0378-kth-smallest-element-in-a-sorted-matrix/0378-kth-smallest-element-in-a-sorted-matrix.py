class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []
        ans = 0
        for i, l in enumerate(matrix):
            heapq.heappush(h, (l[0], i, 0))
        
        for _ in range(k):
            ans, i, cur = heapq.heappop(h)
            if cur + 1 < len(matrix[i]):
                heapq.heappush(h,(matrix[i][cur + 1], i, cur + 1))
        
        return ans
        