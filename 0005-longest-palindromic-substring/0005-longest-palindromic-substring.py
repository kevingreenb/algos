class Solution:
    def longestPalindrome(self, s: str) -> str:
        def explore(left, right):
            q = deque()
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if left == right:
                    q.append(s[left])
                else:
                    q.appendleft(s[left])
                    q.append(s[right])
                left -= 1
                right += 1
            return q

        ans = []
        for i in range(len(s)):
            odd = explore(i, i)
            even = explore(i, i+1)
            longer = odd if len(odd) > len(even) else even
            ans = longer if len(longer) > len(ans) else ans
        return "".join(ans)

        