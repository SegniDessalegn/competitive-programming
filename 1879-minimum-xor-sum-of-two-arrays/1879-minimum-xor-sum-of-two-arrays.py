class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        
        dp = [[float("inf")] * (1 << N) for _ in range(N + 1)]
        dp[0][0] = 0
        
        for i in range(N):
            for mask in range(1 << N):
                if dp[i][mask] == float("inf"):
                    continue
                
                for j in range(N):
                    if not(mask & (1 << j)):
                        next_mask = mask | (1 << j)
                        dp[i + 1][next_mask] = min(dp[i + 1][next_mask], dp[i][mask] + (nums1[i] ^ nums2[j]))
        
        return dp[N][(1 << N) - 1]
    