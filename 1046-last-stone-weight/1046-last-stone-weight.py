class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        heapq._heapify_max(stones)
        while len(stones) > 1:
            largest = heapq._heappop_max(stones)
            second  = heapq._heappop_max(stones)
            if largest != second:
                stones.append(largest - second)
                heapq._siftdown_max(stones, 0, len(stones) - 1)

        return stones[0] if stones else 0