class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, cur = [], []
        def backtrack(i, s):
            if s == target:
                ans.append(cur[:])
                return
            elif s >= target:
                return
            for j in range(i, len(candidates)):
                cur.append(candidates[j])
                backtrack(j, s+candidates[j])
                cur.pop()
        backtrack(0, 0)
        return ans
        