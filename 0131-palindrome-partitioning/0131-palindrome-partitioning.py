class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans, cur = [], []
        def is_palin(s2):
            return s2 == s2[::-1]

        def dfs(i):
            if i >= len(s):
                ans.append(cur[:])
                return
            for j in range(i, len(s)):
                s2 = s[i : j + 1]
                if is_palin(s2):
                    cur.append(s2)
                    dfs(j + 1)
                    cur.pop()
        dfs(0)
        return ans