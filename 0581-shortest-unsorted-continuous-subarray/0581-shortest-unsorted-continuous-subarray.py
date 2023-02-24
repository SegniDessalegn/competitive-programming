class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left <= right and (nums[left] == nums_sorted[left] or nums[right] == nums_sorted[right]):
            if nums[left] == nums_sorted[left]:
                left += 1
            if nums[right] == nums_sorted[right]:
                right -= 1
        
        return max(0, right - left + 1)