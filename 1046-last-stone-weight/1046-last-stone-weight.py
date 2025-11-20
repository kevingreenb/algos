class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            dif = first-second
            if dif == 0:
                continue
            heapq.heappush(stones, -abs(dif))
            
        return -stones[0] if stones else 0
        