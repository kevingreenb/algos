class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        count1 = [0]*26
        count2 = [0]*26

        for c in s1:
            count1[ord(c)-ord("a")] += 1

        left = 0
        for right, c in enumerate(s2):
            count2[ord(c)-ord("a")] += 1
            if right - left >= len(s1):
                count2[ord(s2[left])-ord("a")] -= 1
                left += 1
            if count1 == count2:
                return True
        return False       

