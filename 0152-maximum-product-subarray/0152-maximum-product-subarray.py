class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        max_val, min_val = 1, 1
        for num in nums:
            temp = max_val * num
            max_val = max(num, max_val * num, min_val * num)
            min_val = min(num, temp, min_val * num)
            ans = max(ans, max_val)
        return ans
        