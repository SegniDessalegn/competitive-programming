class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def recurse(i):
            nonlocal dp
            if dp[i] is not None:
                return dp[i]
            curr_ans = [1]
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    curr_ans.append(1 + recurse(j))
            dp[i] = max(curr_ans)
            return dp[i]
        
        dp = [None for _ in range(len(nums))]
        for i in range(len(nums)):
            if dp[i] is None:
                recurse(i)
        
        return max(dp)