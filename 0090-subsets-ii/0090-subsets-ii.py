class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cur, ans = [], []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                ans.append(cur[:])
                return
            cur.append(nums[i])
            backtrack(i + 1)
            cur.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return ans
