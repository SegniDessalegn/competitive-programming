class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        @cache
        def get_ans(i, left, right):
            if i == N:
                return left == right
            
            if left > s // 2 or right > s // 2:
                return False
            
            if get_ans(i + 1, left + nums[i], right):
                return True
            
            if get_ans(i + 1, left, right + nums[i]):
                return True
        
        N = len(nums)
        s = sum(nums)
        return get_ans(0, 0, 0)
    