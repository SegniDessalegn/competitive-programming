class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        s = sum(nums)
        if s % 2 == 1:
            return False
        maxVal = max(nums) * N + 1
        
        dp = [[False] * maxVal for _ in range(N + 1)]
        dp[0][0] = True
        for i in range(1, N + 1):
            for j in range(maxVal):
                if dp[i-1][j] == True:
                    dp[i][j] = True
                    dp[i][j + nums[i-1]] = True
                
                if j == s // 2 and dp[i][j] == True:
                    return True
        
        return False
    