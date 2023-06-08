class Solution:
    def jump(self, nums: List[int]) -> int:
        
        def recur(i):
            if i == n - 1:
                return 0
            elif i >=n or nums[i] == 0:
                return float("inf")
            
            if i in dp:
                return dp[i]
            
            min_steps = float("inf")
            for step in range(1, nums[i] + 1):
                min_steps = min(min_steps, 1 + recur(i + step))
            
            dp[i] = min_steps
            
            return dp[i]
        
        
        n = len(nums)
        dp = {}
        return recur(0)