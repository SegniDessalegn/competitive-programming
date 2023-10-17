class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        @cache
        def get_ans(i, balance):
            if i == N:
                return balance == s // 2
            
            if abs(balance) > s // 2:
                return False
            
            if get_ans(i + 1, balance + nums[i]):
                return True
            
            if get_ans(i + 1, balance):
                return True
        
        N = len(nums)
        s = sum(nums)
        if s % 2 == 1:
            return False
        return get_ans(0, 0)
    