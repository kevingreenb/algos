class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = "+-/*"
        stack = []
        for c in tokens:
            if c not in ops:
                stack.append(c)
                continue
            second = int(stack.pop())
            first = int(stack.pop())
            if c == "+":
                stack.append(first + second)
            elif c == "-":
                stack.append(first - second)
            elif c == "/":
                stack.append(first / second)
            elif c == "*":
                stack.append(first * second)
            
        return int(stack[-1])
        