class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [a, b, c, d]
        # [1, a, ab, abc]
        # [bcd, acd, abd, abc]

        ans = [1]*len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i-1]*nums[i-1]

        multiplier = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= multiplier
            multiplier *= nums[i]

        return ans
        