class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        @cache
        def get_ans(mask, s, curr):
            if mask == (1 << N) - 1:
                return s == each and curr == k - 1
            
            if s > each or curr >= k:
                return False
            
            for i in range(N):
                if not (mask & (1 << i)):
                    if get_ans(mask | (1 << i), nums[i] + (s if s != each else 0), curr + (0 if s != each else 1)):
                        return True
            
            return False
        
        N = len(nums)
        s = sum(nums)
        if s % k != 0:
            return False
        
        each = s // k
        return get_ans(0, 0, 0)
    