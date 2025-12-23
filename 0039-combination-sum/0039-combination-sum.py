class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, cur = [], []
        def helper(i, s):
            if s == target:
                ans.append(cur[:])
                return
            if s > target:
                return
            for j in range(i, len(candidates)):
                cur.append(candidates[j])
                helper(j, s+candidates[j])
                cur.pop()
        helper(0, 0)
        return ans
        