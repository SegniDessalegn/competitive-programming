class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        dp = [float("inf")] * (N + 1)
        dp[0] = 0
        passes = [1, 7, 30]
        for i in range(1, N + 1):
            for j in range(3):
                idx = bisect_left(days, days[i - 1] - passes[j] + 1)
                dp[i] = min(dp[i], costs[j] + dp[idx])
        
        return dp[-1]
    