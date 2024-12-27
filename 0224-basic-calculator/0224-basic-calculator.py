class Solution:
    def calculate(self, s: str) -> int:
        def get_number(i):
            num = 0
            while i < len(s) and s[i] not in "+-=() ":
                num = num * 10 + int(s[i])
                i += 1
            return (num, i)
        
        s = "(" + s + ")"
        stack = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == ")":
                num = 0
                while stack[-1] != "(":
                    if stack[-1] == "-":
                        num *= -1
                    elif stack[-1] != "+":
                        num += stack[-1]
                    stack.pop()
                stack.pop()
                if stack and stack[-1] == "-":
                    stack.pop()
                    stack.append(num * -1)
                else:
                    stack.append(num)
            elif s[i] in "+-":
                stack.append(s[i])
            else:
                num, i = get_number(i)
                if stack and stack[-1] == "+" and stack[-2] != "(":
                    stack.pop()
                    stack[-1] += num
                elif stack and stack[-1] == "-" and stack[-2] != "(":
                    stack.pop()
                    stack[-1] -= num
                else:
                    if stack and stack[-1] == "-":
                        stack.pop()
                        stack.append(num * -1)
                    else:
                        stack.append(num)
                continue
            i += 1
        
        return stack[0]
    