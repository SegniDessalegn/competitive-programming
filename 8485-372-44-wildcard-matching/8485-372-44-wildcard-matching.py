class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M = len(s)
        N = len(p)
        dp = [[False for _ in range(N + 1)] for __ in range(M + 1)]
        dp[0][0] = True
        
        for j in range(1, N + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]
        
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - 1] or dp[i][j - 1]
                elif p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = s[i - 1] == p[j - 1] and dp[i - 1][j - 1]
        
        return dp[-1][-1]
        