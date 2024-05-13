class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        
        @cache
        def get_ans(i, mask):
            if mask == (1 << N) - 1:
                return 0
            
            curr = float("inf")
            for j in range(N):
                if not (mask & (1 << j)):
                    curr = min(curr, (nums1[i] ^ nums2[j]) + get_ans(i + 1, mask | (1 << j)))
            
            return curr
        
        return get_ans(0, 0)
    