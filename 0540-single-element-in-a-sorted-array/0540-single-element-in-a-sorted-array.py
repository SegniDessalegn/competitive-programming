class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            index = (left + right) // 2
            if nums[index - 1] != nums[index] != nums[index + 1]:
                return nums[index]
            if nums[index - 1] == nums[index]:
                if (index - left + 1) % 2 == 0:
                    left = index + 1
                else:
                    right = index
            else:
                if (right - index + 1) % 2 == 0:
                    right = index - 1
                else:
                    left = index
        
        return nums[right]