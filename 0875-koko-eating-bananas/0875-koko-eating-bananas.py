class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_valid(a, h):
            current = 0
            for pile in piles:
                current += math.ceil(pile/a)
                if current > h:
                    return False
            return True
        ans, left = 0, 1
        right = max(piles)
        while left <= right:
            mid = (right+left)//2
            if is_valid(mid, h):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

        