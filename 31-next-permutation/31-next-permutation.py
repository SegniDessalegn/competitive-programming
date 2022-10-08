class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        i -= 1
        j = -1
        while j > -len(nums) + i and nums[i] >= nums[j]:
            j -= 1
        if j <= -len(nums):
            j = -1
        nums[i], nums[j] = nums[j], nums[i]
        arr = nums[i + 1:]
        arr.sort()
        nums[:] = nums[:i + 1] + arr