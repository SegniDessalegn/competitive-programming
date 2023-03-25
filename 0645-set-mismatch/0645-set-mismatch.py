class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            corr_index = nums[i] - 1
            if corr_index >= len(nums):
                continue
            if nums[corr_index] != nums[i]:
                nums[corr_index], nums[i] = nums[i], nums[corr_index]
            else:
                i += 1
        
        errors = []
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                errors.append(nums[i])
                errors.append(i + 1)
        
        return errors