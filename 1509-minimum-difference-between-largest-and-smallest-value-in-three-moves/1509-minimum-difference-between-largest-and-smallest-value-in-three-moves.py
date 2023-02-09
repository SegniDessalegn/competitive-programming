class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        l = 0
        r = len(nums) - 1
        return min(nums[r] - nums[l + 3], nums[r - 1] - nums[l + 2], nums[r - 2] - nums[l + 1], nums[r - 3] - nums[l])