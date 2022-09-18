class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        counter = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i - 1]:
                difference = nums[i - 1] - nums[i]
                counter += difference + 1
                nums[i] = nums[i] + difference + 1
        return counter