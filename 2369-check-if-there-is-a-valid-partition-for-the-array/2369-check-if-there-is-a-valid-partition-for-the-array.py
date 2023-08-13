class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        
        dp = [True]
        for i in range(1, N + 1):
            current = False
            current |= i >= 2 and nums[i - 1] == nums[i - 2] and dp[i - 2]
            current |= i >= 3 and nums[i - 1] == nums[i - 2] == nums[i - 3] and dp[i - 3]
            current |= i >= 3 and nums[i - 1] == nums[i - 2] + 1 and nums[i - 2] == nums[i - 3] + 1 and dp[i - 3]
            
            dp.append(current)
        
        return dp[N]