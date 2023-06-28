class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = {}
        def recur(i):
            if i >= n:
                return 0
            if i in dp:
                return dp[i]
            
            dp[i] = cost[i] + min(recur(i + 1), recur(i + 2))
            return dp[i]
        
        n = len(cost)
        recur(0)
        recur(1)
        
        return min(dp[0], dp[1])