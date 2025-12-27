class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = "+-*/"
        stack = []
        for token in tokens:
            if token not in ops:
                stack.append(token)
                continue
            second = int(stack.pop())
            first = int(stack.pop())
            if token == "+":
                stack.append(first + second)
            elif token == "-":
                stack.append(first - second)
            elif token == "*":
                stack.append(first * second)
            elif token == "/":
                stack.append(first / second)
        return int(stack[0])
        