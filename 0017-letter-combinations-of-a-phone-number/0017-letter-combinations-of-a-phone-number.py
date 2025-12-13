class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        ans, cur = [], []
        def dfs(i):
            if i >= len(digits):
                ans.append("".join(cur))
                return
            d = digits[i]
            for c in phone[int(d)]:
                cur.append(c)
                dfs(i + 1)
                cur.pop()
        dfs(0)
        return ans

        