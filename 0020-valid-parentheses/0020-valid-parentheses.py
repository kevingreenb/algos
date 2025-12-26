class Solution:
    def isValid(self, s: str) -> bool:
        p = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack or p[c] != stack[-1]:
                    return False
                stack.pop()
        return not stack