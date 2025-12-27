class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            if not stack or temperatures[stack[-1]] >= temp:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temp:
                    ans[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return ans