class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        counter = 0
        for char in s:
            if char == ")":
                if not stack:
                    counter += 1
                else:
                    stack.pop()
            else:
                stack.append(char)
        counter += len(stack)
        return counter