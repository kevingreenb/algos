class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        current = sum(nums)
        expected = int((n*(n+1))/2)
        return expected - current

        