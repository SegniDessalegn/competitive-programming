class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        invalid = set()
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    invalid.add(i)
        
        stack = set(stack)
        valid = ""
        for i in range(len(s)):
            if i not in stack and i not in invalid:
                valid += s[i]
        
        return valid