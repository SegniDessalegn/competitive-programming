class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        def get_less_than(val):
            result = 0
            left = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] <= val:
                    result += (right - left)
                    left += 1
                else:
                    right -= 1
            
            return result
        
        nums.sort()
        return get_less_than(upper) - get_less_than(lower - 1)
    