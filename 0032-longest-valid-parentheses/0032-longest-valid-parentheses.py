class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [["", 0]]
        N = len(s)
        ans = 0
        for i in range(N):
            if s[i] == ")":
                if stack[-1][0] == "(":
                    popped = stack.pop()
                    stack[-1][1] += popped[1] + 2
                    ans = max(ans, stack[-1][1])
                else:
                    stack.append([")", 0])
            else:
                stack.append(["(", 0])
        
        return ans
    