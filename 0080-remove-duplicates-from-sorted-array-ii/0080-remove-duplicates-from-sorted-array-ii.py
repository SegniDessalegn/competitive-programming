class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        duplicate = False
        length = 0
        while j < len(nums):
            while duplicate and j < len(nums) and nums[j] == nums[j - 1]:
                j += 1
            if duplicate and j < len(nums) and nums[j] != nums[j - 1]:
                duplicate = False
            if j > 0 and j < len(nums) and nums[j] == nums[j - 1]:
                duplicate = True
            if j < len(nums):
                nums[i] = nums[j]
                length += 1
            i += 1
            j += 1
        return length