class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")" : "(", "}" : "{", "]" : "["}
        opens = "({["
        stack = []
        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
        return not stack
        