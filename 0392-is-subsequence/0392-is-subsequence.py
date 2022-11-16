class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i, j = 0, 0
        while j < len(t):
            if i < len(s) and t[j] == s[i]:
                i += 1
            if i >= len(s):
                return True
            j += 1
        return False