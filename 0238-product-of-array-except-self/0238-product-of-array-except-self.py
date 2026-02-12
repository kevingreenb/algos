class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [a, b, c, d]
        # [1, a, ab, abc]
        # [bcd,acd,abd,abc]
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        multiplier = 1
        for i in range(n-1, -1, -1):
            ans[i] *= multiplier
            multiplier *= nums[i]
        return ans
        