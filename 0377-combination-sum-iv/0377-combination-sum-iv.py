class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        @cache
        def back_track(curr):            
            if curr == target:
                return 1
            elif curr > target:
                return 0
            
            curr_ans = 0
            for j in range(n):
                curr_ans += back_track(curr + nums[j])
            
            return curr_ans
        
        return back_track(0)