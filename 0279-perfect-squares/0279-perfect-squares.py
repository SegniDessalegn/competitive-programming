class Solution:
    def numSquares(self, n: int) -> int:
        dp = defaultdict(lambda : float("inf"))
        dp[0] = 0
        
        for num in range(n + 1):
            i = 1
            while i * i <= num:
                square = i * i
                dp[num] = min(dp[num], 1 + dp[num - square])
                i += 1
        
        return dp[n]
    