class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtrack(start, subset):
            res.append(subset[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue        
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        backtrack(0, [])
        return res