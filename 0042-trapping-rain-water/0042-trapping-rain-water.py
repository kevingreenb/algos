class Solution:
    def trap(self, height):
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] < leftMax:
                    water += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1
            else:
                if height[right] < rightMax:
                    water += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1
        
        return water