class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_range(start, end):
            if start > end:
                return 0
            if start == end:
                return nums[start]

            prev2 = nums[start]
            prev1 = max(nums[start], nums[start + 1])

            for i in range(start + 2, end + 1):
                current = max(prev2 + nums[i], prev1)
                prev2 = prev1
                prev1 = current
                
            return prev1
        return max(rob_range(0, n - 2), rob_range(1, n - 1))
