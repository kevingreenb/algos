class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, cur = [], []
        def helper(o, c):
            if len(cur) == (n * 2):
                ans.append("".join(cur))
                return
            if o < n:
                cur.append("(")
                helper(o + 1, c)
                cur.pop()
            if c < o:
                cur.append(")")
                helper(o, c + 1)
                cur.pop()
        helper(0, 0)
        return ans
        