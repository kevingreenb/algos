class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cur, ans = [], []
        nums.sort()
        def backtrack(i):
            ans.append(cur[:])
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                cur.append(nums[j])
                backtrack(j + 1)
                cur.pop()
        backtrack(0)
        return ans
                