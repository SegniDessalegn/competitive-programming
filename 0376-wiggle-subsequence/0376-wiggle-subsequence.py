class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # top-down approach
        # must have two states to know whether the last difference was positive or negative
        
        def recur(i, was_pos):
            if i >= N:
                return 0
            
            if (i, was_pos) in dp:
                return dp[(i, was_pos)]
            
            length = 0
            for j in range(i + 1, N):
                if was_pos:
                    if nums[j] - nums[i] < 0:
                        length = max(length, 1 + recur(j, not was_pos))
                else:
                    if nums[j] - nums[i] > 0:
                        length = max(length, 1 + recur(j, not was_pos))
            
            dp[(i, was_pos)] = length
            return dp[(i, was_pos)]
        
        N = len(nums)
        dp = {}
        for i in range(N):
            recur(i, True)
            recur(i, False)
        
        return max(dp.values()) + 1