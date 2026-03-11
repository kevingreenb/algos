class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, cur = [], []
        def backtrack(start):
            if start == len(nums):
                ans.append(cur.copy())
                return
            cur.append(nums[start])
            backtrack(start + 1)
            cur.pop()
            backtrack(start + 1)
        backtrack(0)
        return ans