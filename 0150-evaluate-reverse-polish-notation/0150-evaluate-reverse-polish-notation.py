class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # 10, 6, -132
        for token in tokens:
            if token in "+-*/":
                second = stack.pop()
                first = stack.pop()
                result = 0
                if token == "+":
                    result = first + second
                elif token == "-":
                    result = first - second
                elif token == "*":
                    result = first * second
                elif token == "/":
                    result = int(first / second)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]
        