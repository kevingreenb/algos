class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            temp = target - num
            if temp in seen:
                return [seen[temp], i]
            seen[num] = i
        return [-1, -1]
        