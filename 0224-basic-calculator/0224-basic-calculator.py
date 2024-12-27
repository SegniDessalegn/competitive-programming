class Solution:
    def calculate(self, s: str) -> int:
        s = "(" + s + ")"
        stack = []
        sign, num = 1, 0
        
        for char in s:
            if char == " ":
                continue
            if char.isdigit():
                num = num * 10 + int(char)
            if char in "+-":
                stack.append(sign * num)
                sign = 1 if char == "+" else -1
                num = 0
            if char == "(":
                stack.append(sign)
                stack.append("(")
                sign, num = 1, 0
            if char == ")":
                val = sign * num
                while stack[-1] != "(":
                    val += stack.pop()
                stack.pop()
                stack[-1] *= val
                sign, num = 1, 0
        
        return stack[0]
    