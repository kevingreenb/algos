class Solution:
    def isValid(self, s: str) -> bool:
        p_dict = {")": "(", "}": "{", "]": "["}
        p = "({["
        stack = []
        for c in s:
            if c in p:
                stack.append(c)
            elif not stack or p_dict[c] != stack[-1] :
                return False
            else:
                stack.pop()
        return not stack