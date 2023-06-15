class Solution:
    def maxDepth(self, s: str) -> int:
        open_count = 0
        ans = 0
        for char in s:
            if char == "(":
                open_count += 1
            elif char == ")":
                open_count -= 1
            ans = max(ans, open_count)
        
        return ans