class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        for i in range(2, len(nums)):
            if nums[i] + nums[i - 1] > nums[i - 2]:
                return nums[i] + nums[i - 1] + nums[i - 2]
        return 0
    