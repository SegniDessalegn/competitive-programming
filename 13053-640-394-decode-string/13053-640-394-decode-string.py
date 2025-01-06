class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                stack.append(str(num))
                num = 0
            elif char == "]":
                curr = []
                while not stack[-1].isdigit():
                    curr.append(stack.pop())
                curr = curr[::-1]
                stack.append(int(stack.pop()) * "".join(curr))
            else:
                stack.append(char)
        
        return "".join(stack)
    