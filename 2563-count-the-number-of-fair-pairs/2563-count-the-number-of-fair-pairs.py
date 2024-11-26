class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        def get_pairs(upper):
            curr_ans = 0
            left = 0
            right = N - 1
            
            while left < right:
                if nums[left] + nums[right] > upper:
                    right -= 1
                else:
                    curr_ans += right - left
                    left += 1
            
            return curr_ans
        
        
        N = len(nums)
        nums.sort()
        return get_pairs(upper) - get_pairs(lower - 1)
    