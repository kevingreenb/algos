class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d = [0]*26
        d2 = [0]*26
        for c in s1:
            d[ord(c)-ord("a")] += 1

        left = 0
        for i in range(len(s2)):
            if (i - left) >= len(s1):
                d2[ord(s2[left])-ord("a")] -= 1
                left += 1
            d2[ord(s2[i])-ord("a")] += 1
            if d2 == d:
                return True
        return False