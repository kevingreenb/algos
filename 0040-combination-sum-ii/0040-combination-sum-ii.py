class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans, cur = [], []
        def helper(i, s):
            if s == target:
                ans.append(cur[:])
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if s + candidates[j] > target:
                    break
                cur.append(candidates[j])
                helper(j + 1, s + candidates[j])
                cur.pop()
        helper(0, 0)
        return ans
        