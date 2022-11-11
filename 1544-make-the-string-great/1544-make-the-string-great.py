class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        for i in range(1, len(s)):
            if stack and s[i].lower() == stack[-1].lower() and ((s[i].islower() and stack[-1].isupper()) or (s[i].isupper() and stack[-1].islower())):
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)