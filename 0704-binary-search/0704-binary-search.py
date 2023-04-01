class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)
        while right - left > 1:
            index = (right + left) // 2
            if nums[index] > target:
                right = index
            else:
                left = index
        
        return left if nums[left] == target else -1