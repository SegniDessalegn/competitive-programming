class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0
        
        left = 0
        right = N - 1
        
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] <= nums[mid + 1]:
                left = mid
            else:
                right = mid
        
        if nums[left] <= nums[left + 1]:
            return left + 1
        else:
            return left
        