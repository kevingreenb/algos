class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        ans, most_freq, left = 0, 0, 0
        for i, c in enumerate(s):
            count[c] += 1
            most_freq = max(most_freq, count[c])
            while (i - left + 1 - most_freq) > k:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans