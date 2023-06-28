class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for i in range(-2, n)]
        for i in range(2, n + 2):
            dp[i] = cost[i - 2] + min(dp[i - 1], dp[i - 2])
        
        return min(dp[-1], dp[-2])