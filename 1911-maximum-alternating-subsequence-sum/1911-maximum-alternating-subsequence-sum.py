class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        @cache
        def get_ans(i, is_even):
            if i == N:
                return 0
            
            curr_sum = -float("inf")
            
            # choose
            curr_sum = max(curr_sum, ((1 if is_even else -1) * nums[i]) + get_ans(i + 1, not is_even))
            
            # not choose
            curr_sum = max(curr_sum, get_ans(i + 1, is_even))
            
            return curr_sum
        
        N = len(nums)
        return get_ans(0, True)
    