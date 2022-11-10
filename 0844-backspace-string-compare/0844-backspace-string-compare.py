class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for c in s:
            if stack1 and c == "#":
                stack1.pop()
            elif c != "#":
                stack1.append(c)
        for c in t:
            if stack2 and c == "#":
                stack2.pop()
            elif c != "#":
                stack2.append(c)
        return True if stack1 == stack2 else False
