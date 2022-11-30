class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right] or len(nums) == 1:
            return nums[left]
        while left <= right:
            index = (right + left) // 2
            if nums[index] >= nums[0]:
                left = index + 1
            else:
                right = index - 1
        if nums[left] > nums[right]:
            start = right
        else:
            start = left
        return nums[start]