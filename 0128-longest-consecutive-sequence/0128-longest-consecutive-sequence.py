class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)

        ans = 0
        for num in st:
            if num-1 in st:
                continue
            streak = 1
            current = num
            while current+1 in st:
                streak += 1
                current += 1
            ans = max(ans, streak)

        return ans
        