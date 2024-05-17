class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        
        dp = [float("inf")] * (1 << N)
        dp[0] = 0
        
        for mask in range(1 << N):
            count = bin(mask).count('1')
            for j in range(N):
                if not (mask & (1 << j)):
                    next_mask = mask | (1 << j)
                    dp[next_mask] = min(dp[next_mask], dp[mask] + (nums1[count] ^ nums2[j]))
        
        return dp[(1 << N) - 1]
    