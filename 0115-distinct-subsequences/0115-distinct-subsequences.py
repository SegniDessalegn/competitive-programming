class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        S = len(s)
        T = len(t)
        
        dp = [[0] * (T + 1) for _ in range(S + 1)]
        for i in range(S + 1):
            dp[i][0] = 1
        
        for i in range(1, S + 1):
            for j in range(1, T + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                dp[i][j] += dp[i - 1][j]
        
        return dp[-1][-1]
    