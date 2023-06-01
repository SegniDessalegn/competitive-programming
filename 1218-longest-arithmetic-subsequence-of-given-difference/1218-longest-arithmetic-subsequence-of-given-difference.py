class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        n = len(arr)
        ans = 1
        for i in range(n):
            dp[arr[i]] = 1 + dp[arr[i] - difference]
            ans = max(ans, dp[arr[i]])
        
        return ans