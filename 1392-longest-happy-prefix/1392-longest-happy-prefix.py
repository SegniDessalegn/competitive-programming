class Solution:
    def longestPrefix(self, s: str) -> str:
        # KMP algorithm
        
        N = len(s)
        LPS = [0] * N
        
        j = 0
        for i in range(1, N):
            while j > 0 and s[i] != s[j]:
                j = LPS[j - 1]
            if s[i] == s[j]:
                j += 1
            LPS[i] = j
        
        return s[:LPS[-1]]