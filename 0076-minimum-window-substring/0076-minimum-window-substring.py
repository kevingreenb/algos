class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        count_t = Counter(t)
        count_s = defaultdict(int)
        needed = len(count_t)
        left = formed = 0
        ans_len = float("inf")
        ans = [0, 0]
        for right, c in enumerate(s):
            count_s[c] += 1
            if c in count_t and count_t[c] == count_s[c]:
                needed -= 1
            while needed == 0 and left <= right:
                if right - left + 1 < ans_len:
                    ans = [left, right]
                    ans_len = right - left + 1
                c2 = s[left]
                count_s[c2] -= 1
                if c2 in count_t and count_s[c2] < count_t[c2]:
                    needed += 1     
                left += 1
        return "" if ans_len == float("inf") else s[ans[0] : ans[1] + 1]