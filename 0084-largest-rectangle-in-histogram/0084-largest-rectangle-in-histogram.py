class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.append(0)
        stack = [] 
        max_area = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # If stack is empty, width spans from 0 to i-1 -> i
                # else width spans from stack[-1]+1 to i-1 -> i - stack[-1] - 1
                width = i if not stack else i - stack[-1] - 1
                area = height * width
                if area > max_area:
                    max_area = area
            stack.append(i)

        return max_area
