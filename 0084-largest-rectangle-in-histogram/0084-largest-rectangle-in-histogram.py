class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        heights.append(0)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                ans = max(ans, (i - index) * height)
                start = index
            stack.append((start, h))
        
        return ans