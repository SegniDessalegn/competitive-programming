class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right] or len(nums) == 1:
            return nums[left]
        curr_min = min(nums[left], nums[right])
        while left <= right:
            index = (right + left) // 2
            if nums[left] == nums[right]:
                right -= 1
            elif nums[index] >= nums[0]:
                curr_min = min(curr_min, nums[left])
                left = index + 1
            else:
                curr_min = min(curr_min, nums[right])
                right = index - 1
            curr_min = min(curr_min, nums[index])
        return curr_min
        
