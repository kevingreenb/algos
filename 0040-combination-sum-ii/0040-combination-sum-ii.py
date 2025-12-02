class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(i, cur, s):
            if s == target:
                ans.append(cur[:])
            elif s > target:
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                cur.append(candidates[j])
                backtrack(j+1,cur, s+candidates[j])
                cur.pop()
        backtrack(0, [], 0)
        return ans
        