class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left, right):
            current = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                current += 1
                left -= 1
                right += 1

            return current

        ans = 0
        for i in range(len(s)):
            ans += expand(i, i)
            ans += expand(i, i+1)
        return ans
        