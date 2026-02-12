class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, ans = prices[0], 0
        for num in prices:
            if num < buy:
                buy = num
            else:
                ans = max(ans, num - buy)
        return ans
        