class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        count = 0
        left = 0
        right = 1
        curr_diff = nums[right] - nums[left]
        while right < len(nums):
            if nums[right] - nums[right - 1] == curr_diff:
                if right - left + 1 >= 3:
                    count += right - left - 1
            else:
                curr_diff = nums[right] - nums[right - 1]
                left = right - 1
            right += 1
        
        return count