class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, ans = prices[0], 0
        for price in prices:
            ans = max(ans, price - buy)
            buy = min(buy, price)
        return ans
        