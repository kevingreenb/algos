class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, left, most_freq = 0, 0, 0
        count = defaultdict(int)
        for i, c in enumerate(s):
            count[c] += 1
            most_freq = max(most_freq, count[c])
            while i - left + 1 - most_freq > k:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans
        