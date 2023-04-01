class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # cyclic sort
        # put every element to the correct position
        # after doing cyclic sort, for every index i, if we can't find the corresponding element, then the element i + 1 is missing from the array
        
        i = 0
        while i < len(nums):
            corr_index = nums[i] - 1
            if corr_index >= len(nums):
                continue
            if nums[corr_index] != nums[i]:
                nums[corr_index], nums[i] = nums[i], nums[corr_index]
            else:
                i += 1
        
        missings = []
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                missings.append(i + 1)
        
        return missings