class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        ans = 0
        while left < right:
            s = (right - left)*min(height[right], height[left])
            ans = max(ans, s)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans

        