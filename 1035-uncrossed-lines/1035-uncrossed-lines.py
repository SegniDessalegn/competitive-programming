class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        N1 = len(nums1)
        N2 = len(nums2)
        dp = [[0] * (N2 + 1) for _ in range(N1 + 1)]
        for i in range(1, N1 + 1):
            for j in range(1, N2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = max(1 + dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
                dp[i][j] = max(dp[i][j], dp[i][j - 1], dp[i - 1][j])
        
        return dp[-1][-1]
