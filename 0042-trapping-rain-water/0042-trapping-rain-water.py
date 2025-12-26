class Solution:
    def trap(self, height: List[int]) -> int:
        r = len(height)-1
        ans, l, lm, rm = 0, 0, 0, 0
        while l < r:
            if height[l] < height[r]:
                if height[l] < lm:
                    ans += lm - height[l]
                else:
                    lm = height[l]
                l += 1
            else:
                if height[r] < rm:
                    ans += rm - height[r]
                else:
                    rm = height[r]
                r -= 1
        return ans 