class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                index += 1
            elif index != 0:
                nums[i - index] = nums[i]
                nums[i] = 0
            i += 1