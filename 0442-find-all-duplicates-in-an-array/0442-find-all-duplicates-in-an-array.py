class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # cyclic sort
        # do cyclic sort and then any element that appears in a wrong position is duplicate
        
        i = 0
        while i < len(nums):
            corr_index = nums[i] - 1
            if corr_index >= len(nums):
                continue
            if nums[corr_index] != nums[i]:
                nums[corr_index], nums[i] = nums[i], nums[corr_index]
            else:
                i += 1
        
        duplicate = []
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                duplicate.append(nums[i])
        
        return duplicate