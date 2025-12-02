class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(i, cur):
            if i == len(nums):
                ans.append(cur[:])
                return
            cur.append(nums[i])
            backtrack(i+1,cur)
            cur.pop()
            backtrack(i+1,cur)
        backtrack(0,[])
        return ans