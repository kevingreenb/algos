class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, cur = [], []
        def backtrack(o, c):
            if len(cur) == 2 * n:
                ans.append("".join(cur))
                return
            if o < n:
                cur.append("(")
                backtrack(o + 1, c)
                cur.pop()
            if c < o:
                cur.append(")")
                backtrack(o, c + 1)
                cur.pop()
        backtrack(0, 0)
        return ans
        