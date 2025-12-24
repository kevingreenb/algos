class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans, cur = [], []
        def is_valid(s2):
            if s2 == s2[::-1]:
                return True
        def helper(i):
            if i == len(s):
                ans.append(cur[:])
                return
            for j in range(i, len(s)):
                s2 = s[i:j+1]
                if is_valid(s2):
                    cur.append(s2)
                    helper(j + 1)
                    cur.pop()
        helper(0)
        return ans
        