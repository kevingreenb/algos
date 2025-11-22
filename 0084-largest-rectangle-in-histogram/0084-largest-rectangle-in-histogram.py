class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Append a 0 to flush remaining bars at the end
        heights = heights + [0]
        stack = []  # will store indices of bars with increasing heights
        max_area = 0

        for i, h in enumerate(heights):
            # While current bar is lower than the bar at stack top,
            # compute area with the bar at top as the smallest bar.
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
