class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[-float("inf")] * 2 for _ in range(N + 1)]
        dp[0][1] = 0
        for i in range(1, N + 1):
            dp[i][0] = max(dp[i][0], dp[i - 1][0], nums[i - 1] + dp[i - 1][1])
            dp[i][1] = max(dp[i][1], dp[i - 1][1], -nums[i - 1] + dp[i - 1][0])
        
        return max(dp[-1])
    