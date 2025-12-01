class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(piles, h, k):
            needed = 0
            for pile in piles:
                needed += math.ceil(pile/k)
                if needed > h:
                    return False
            return needed <= h
        
        left, right = 1, max(piles)
        ans = -1
        while left <= right:
            mid = (right+left)//2
            if canFinish(piles, h, mid):
                ans = mid
                right = mid -1
            else: 
                left = mid + 1
        return ans