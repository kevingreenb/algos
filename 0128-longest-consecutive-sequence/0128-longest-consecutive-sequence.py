class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for num in num_set:
            if num-1 not in num_set:
                current = num
                streak = 0
                while current in num_set:
                    streak += 1
                    current += 1
                ans = max(ans, streak)
        return ans