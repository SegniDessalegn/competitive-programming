class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        N = len(weights)
        k_pos = []
        for i in range(1, N):
            k_pos.append(weights[i] + weights[i - 1])
        
        k_pos.sort()
        
        min_ks = sum(k_pos[:k - 1])
        max_ks = sum(k_pos[N - k:])
        
        return max_ks - min_ks