class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "]":
                cur = ""
                while stack and stack[-1] != "[":
                    cur = stack.pop() + cur
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(cur * int(num))
            else:
                stack.append(i)

        return "".join(stack)
