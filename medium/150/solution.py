from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in "+-*/":
                right = stack.pop()
                left = stack.pop()

                if i == "+":
                    stack.append(left + right)
                elif i == "-":
                    stack.append(left - right)
                elif i == "*":
                    stack.append(left * right)
                elif i == "/":
                    stack.append(int(left / right))
            else:
                stack.append(int(i))

        return stack[0]
