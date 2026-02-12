class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        for c in t:
            if count[c] == 0:
                return False
            count[c] -= 1
        return True