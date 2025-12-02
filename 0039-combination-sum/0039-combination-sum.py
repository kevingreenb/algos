class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(i, cur, c_sum):
            if c_sum == target:
                ans.append(cur[:])
                return
            elif c_sum > target:
                return
            for j in range(i, len(candidates)):
                cur.append(candidates[j])
                backtrack(j,cur,c_sum+candidates[j])
                cur.pop()
        backtrack(0,[],0)
        return ans
        