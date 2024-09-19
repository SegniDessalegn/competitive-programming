class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        N = len(energyDrinkA)
        dp = [[0, 0] for i in range(N + 2)]
        
        for i in range(2, N + 2):
            dp[i][0] = max(dp[i][0], energyDrinkA[i - 2] + max(dp[i - 1][0], dp[i - 2][1]))
            dp[i][1] = max(dp[i][1], energyDrinkB[i - 2] + max(dp[i - 1][1], dp[i - 2][0]))
        
        return max(dp[-1][0], dp[-1][1])
    