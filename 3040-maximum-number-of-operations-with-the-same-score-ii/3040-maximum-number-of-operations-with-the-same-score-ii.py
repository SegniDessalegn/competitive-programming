class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
        @cache
        def get_ans(i, j, target):
            if i >= j:
                return 0
            
            operations = 0
            if nums[i] + nums[i + 1] == target:
                operations = max(operations, 1 + get_ans(i + 2, j, target))
            if nums[j] + nums[j - 1] == target:
                operations = max(operations, 1 + get_ans(i, j - 2, target))
            if nums[i] + nums[j] == target:
                operations = max(operations, 1 + get_ans(i + 1, j - 1, target))
            
            return operations
        
        
        N = len(nums)
        operations = 0
        return max(get_ans(0, N - 1, nums[0] + nums[1]),
                   get_ans(0, N - 1, nums[N - 1] + nums[N - 2]),
                   get_ans(0, N - 1, nums[0] + nums[N - 1]))
        