class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        left, ans = 0, 0
        for i, c in enumerate(s):
            left = max(d.get(c,-1)+1,left)
            d[c] = i
            ans = max(ans,i-left+1)
        return ans

        