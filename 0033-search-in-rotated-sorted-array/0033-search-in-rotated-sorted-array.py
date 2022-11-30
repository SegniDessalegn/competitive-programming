class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] < nums[-1] or len(nums) == 1:
            return self.bin_search(nums, target)
        else:
            left, right = 0, len(nums) - 1
            while left <= right:
                index = (right + left) // 2
                if nums[index] >= nums[0]:
                    left = index + 1
                else:
                    right = index - 1
            if nums[left] > nums[right]:
                pivot = right
            else:
                pivot = left
            if nums[0] <= target <= nums[pivot - 1]:
                return self.bin_search(nums[:pivot], target)
            elif nums[pivot] <= target <= nums[-1]:
                index = self.bin_search(nums[pivot:], target)
                if index != -1:
                    return pivot + index
            return -1
        
    def bin_search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            index = (right + left) // 2
            if nums[index] > target:
                right = index - 1
            elif nums[index] < target:
                left = index + 1
            else:
                return index
        return -1